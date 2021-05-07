
# https://towardsdatascience.com/backpropagation-in-a-convolutional-layer-24c8d64d8509
class ConvImage(object):
    def __init__(self,inputs, n_filters, filter_h, filter_w):
        import numpy as np
        self.inputs = inputs
        self.n_filters = n_filters
        self.filter_h = filter_h
        self.filter_w = filter_w
        
        self.channel = inputs.shape[0]
        self.input_h = inputs.shape[1]
        self.input_w = inputs.shape[2]
        
        #(filters, channel, HH, WW)
        self.weights = np.ones([self.n_filters, self.channel, filter_size, filter_size])
        
    def forward(self):
        self.y = np.zeros([self.n_filters, self.input_h - self.filter_h + 1, self.input_w - self.filter_w + 1])
        
        for f in range(self.n_filters):
            for i in range(self.y.shape[1]):
                for j in range(self.y.shape[2]):
                    #conv ops
                    tmp = 0
                    for k in range(self.filter_h):
                        for l in range(self.filter_w):
                            for c in range(self.channel):
                                tmp += self.inputs[c, i+k, j+l]*self.weights[f,c,k,l]
                    self.y[f,i,j] = tmp
        
        return self.y

    
    def backward(self):
        """
        A naive implementation of the backward pass for a convolutional layer.
        Inputs:
        - dout: Upstream derivatives.
        - cache: A tuple of (x, w, b, conv_param) as in conv_forward_naive
        Returns a tuple of:
        - dx: Gradient with respect to x
        - dw: Gradient with respect to w
        - db: Gradient with respect to b
        """

        dx, dw, db = None, None, None

        # retriving variable
        x = self.inputs
        w = self.weights
        b = 0
        pad = 0
        stride = 1
        dout = np.ones_like(self.forward())

        # Initialisations
        dx = np.zeros_like(x)
        dw = np.zeros_like(w)
#         db = np.zeros_like(b)

        # Dimensions
        C, H, W = x.shape
        F, _, HH, WW = w.shape
        _, H_, W_ = dout.shape

        # dw = xp * dy
        # 0-padding just on the last two dimentions of x
        xp = np.pad(x, ((0,), (pad,), (pad, )), 'constant')

        # Version without vectorization

        for f in range(F):   # loop through all the filters
            for i in range(HH): # results indices
                for j in range(WW):
                    for k in range(H_): # indices of filter
                        for l in range(W_):
                            for c in range(C): # depth
                                dw[f,c,i,j] += xp[c, stride*i+k, stride*j+l] * dout[f, k, l]

        # dx = dy_0 * w'
        # Valide seulement pour un stride = 1
        # 0-padding just last two dimention dy = dout (N, F, H', W')
        doutp = np.pad(dout, ((0,), (WW-1,), (HH-1, )), 'constant')

        # 0-padding just last two dimention of dx
        pad = 0
        dxp = np.pad(dx, ((0,), (pad,), (pad, )), 'constant')

        # filtre inversé dimension (F, C, HH, WW)
        w_ = np.zeros_like(w)
        for i in range(HH):
            for j in range(WW):
                w_[:,:,i,j] = w[:,:,HH-i-1,WW-j-1]

        # Version sans vectorisation

        for f in range(F):   # all filters
            for i in range(H+2*pad): # indices in results
                for j in range(W+2*pad):
                    for k in range(HH): # indices du filtre
                        for l in range(WW):
                            for c in range(C): # depth
                                dxp[c,i,j] += doutp[f, i+k, j+l] * w_[f, c, k, l]
        #Remove padding for dx
        
        dx = dxp[:,pad:,pad:]

        return dx, dw      
        
             
import numpy as np
#(channel, H, W)
inputs = np.ones([3,6,7])
filter_h = 2
filter_w = 2
n_filters = 4

conv = ConvImage(inputs, n_filters, filter_h, filter_w)
conv.forward()
dx, dw = conv.backward()
print(dx)
print(dw)
