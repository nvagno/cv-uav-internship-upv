import torch
import torch.nn as nn
from .conv import Conv
from .block import C2f, C3, Bottleneck


class simam_module(torch.nn.Module):
    """Simplified Attention Module (SimAM) - A lightweight attention mechanism without parameters."""
    
    def __init__(self, channels=None, e_lambda=1e-4):
        """Initialize SimAM module with optional channels and lambda parameter."""
        super(simam_module, self).__init__()
        self.activaton = nn.Sigmoid()
        self.e_lambda = e_lambda

    def __repr__(self):
        """Return string representation of the module."""
        s = self.__class__.__name__ + '('
        s += ('lambda=%f)' % self.e_lambda)
        return s

    @staticmethod
    def get_module_name():
        """Return the name of this module."""
        return "simam"

    def forward(self, x):
        """Forward pass through SimAM attention mechanism."""
        b, c, h, w = x.size()
        n = w * h - 1  # Number of spatial locations minus 1
        
        # Calculate attention weights
        x_minus_mu_square = (x - x.mean(dim=[2, 3], keepdim=True)).pow(2)
        y = x_minus_mu_square / (4 * (x_minus_mu_square.sum(dim=[2, 3], keepdim=True) / n + self.e_lambda)) + 0.5
        
        # Apply attention to input features
        return x * self.activaton(y)


class Bottleneck_simam(nn.Module):
    """Standard bottleneck block with SimAM attention integration."""
    
    def __init__(self, c1, c2, shortcut=True, g=1, k=(3, 3), e=0.5):
        """
        Initialize a bottleneck block with SimAM attention.
        
        Args:
            c1 (int): Input channels
            c2 (int): Output channels
            shortcut (bool): Whether to use shortcut connection
            g (int): Groups for convolution
            k (tuple): Kernel sizes for convolutions
            e (float): Expansion ratio
        """
        super().__init__()
        c_ = int(c2 * e)  # Hidden channels
        self.cv1 = Conv(c1, c_, k[0], 1)  # First convolution
        self.cv2 = simam_module(c_)       # SimAM attention
        self.add = shortcut and c1 == c2  # Whether to use shortcut connection

    def forward(self, x):
        """Forward pass through bottleneck with optional shortcut."""
        return x + self.cv2(self.cv1(x)) if self.add else self.cv2(self.cv1(x))


class C3k(C3):
    """
    C3k module with customizable kernel sizes and SimAM attention.
    CSP bottleneck with 3 convolutions and configurable kernel sizes.
    """
    
    def __init__(self, c1, c2, n=1, shortcut=True, g=1, e=0.5, k=3):
        """
        Initialize C3k module with SimAM-enhanced bottlenecks.
        
        Args:
            c1 (int): Input channels
            c2 (int): Output channels
            n (int): Number of bottleneck blocks
            shortcut (bool): Whether to use shortcut connections
            g (int): Groups for convolutions
            e (float): Expansion ratio
            k (int): Kernel size for convolutions
        """
        super().__init__(c1, c2, n, shortcut, g, e)
        c_ = int(c2 * e)  # Hidden channels
        self.m = nn.Sequential(*(Bottleneck_simam(c_, c_, shortcut, g, k=(k, k), e=1.0) for _ in range(n)))


class FlexSimAM(C2f):
    """
    Flexible CSP Bottleneck module with optional SimAM attention blocks.
    Can switch between standard bottlenecks and SimAM-enhanced C3k blocks.
    """
    
    def __init__(self, c1, c2, n=1, c3k=False, e=0.5, g=1, shortcut=True):
        """
        Initialize FlexSimAM module with configurable attention blocks.
        
        Args:
            c1 (int): Input channels
            c2 (int): Output channels
            n (int): Number of bottleneck blocks
            c3k (bool): Whether to use C3k (SimAM) blocks
            e (float): Expansion ratio
            g (int): Groups for convolutions
            shortcut (bool): Whether to use shortcut connections
        """
        super().__init__(c1, c2, n, shortcut, g, e)
        self.m = nn.ModuleList(
            C3k(self.c, self.c, 2, shortcut, g) if c3k 
            else Bottleneck(self.c, self.c, shortcut, g) for _ in range(n)
        )
