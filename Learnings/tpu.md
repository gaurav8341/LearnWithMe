# Google TPU 

- Read about Google TPU's. Based on Systollic arrays. 
- Systollic Arrays is pretty much like a pipeline where like a human heart processing, inflow and out flow of data happens at he same time. 
- In a systollic arrays, the result goes and new input enters the array. Pretty much similar like how the Gstreamer Pipeline should operate. 
- This is good way to do vector arithematics.

**THERE IS GOING TOBE ALOT OF COPY PASTE IN THIS**

## Matrix multiplication in Systoliic way

Consider 2 matrices of dimention 2x2. To perform the matrix multiplication in systolic way it would as shown in figure below

![Systollic matrix multiplication](../static/images/tpu/systolic-mm.webp "Systollic Matrix Multiplication")

It takes 4 steps to do 2x2 matrix multiplication. During starting and ending of the some of the MAC(Multiply/ Accumulate Unit) are not used.

If data is fed in correct order larger matrix multiplication opertation can also be done very efficiently if data is fed in right order to Systollic arrays

Because of above process there is no need to store or load the data to the main memory area. Intermediate results are stored in MAC only. 

## TPU

Googles TPU are made to take advantage of this systollic array architecture. TPU (Tensor Proceesing Unit) is nothing but special ASIC( Application Specific Integrated Circuit). The perform calculations on tensors.


## TPUv1 Architecture


![TPU v1 Architecture -- Simplified](../static/images/tpu/tpu-v1-arch.webp "TPU v1 Architecture -- Simplified")

Initial V1 architecture was only used for inference of the neural networks. 

In V1 architecture PCIE bus was given for communication with main host computer. It also has direct acees to its own DDR3 dynamic ram storage

Rather than be tightly integrated with a CPU, to reduce the chances of delaying deployment, the TPU was designed to be a coprocessor on the PCIe I/O bus, allowing it to plug into existing servers just as a GPU does. Moreover, to simplify hardware design and debugging, the host server sends TPU instructions for it to execute rather than fetching them itself. TPUv1 are more like FPU(Floating Point unit) coprocessor than GPU

1. DDR3 DRAM / Weight FIFO: 
> Weights are stored in DDR3 RAM chips connected to the TPU v1 via DDR3-2133 interfaces. Weights are ‘pre-loaded’ onto these chips from the host computer’s memory via PCIe and can then be transferred into the ‘Weight FIFO’ memory ready for use by the matrix multiply unit.
2. Matrix Multiply Unit:
> This is a ‘systolic’ array with 256 x 256 matrix multiply/accumulate units that is fed by 256 ‘weight’ values from the top and 256 data inputs from the left.
3. Accumulators:
> The results emerge from the systolic matrix unit at the bottom and are stored in ‘accumulator’ memory storage.
4. Activation:
> The activation functions described in the neural network above are applied here.
5. Unified Buffer / Systolic Data Setup: 
> The results of applying the activation functions are stored in a ‘unified buffer’ memory where they are ready to be fed back as inputs to the Matrix Multiply Unit to calculate the values needed for the next layer.

