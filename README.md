# Neurocessor
Neuromorphic packet-based architecture of neural CPU based on traditional GPU nucleus (without memristors)
From my blog: http://taktaev.com/node/202


Mode 1 Network Programming.

Slide 8. Teaching mode is set by the external control. Through the bus is loaded program code emulation neural network with the FROM address: # 00000000. Cores controller programmed so that the instruction code of the address mode is perceived as a software.

Slide 9. If the address «TO:» is a broadcast, (TO: #FFFFFFFF), the code is loaded into all microcontrollers. You can use network masks type # AB.CD.EE.00, which is similar to an IP mask that will load only a portion of the nuclei whose address matches the given mask. This allows different controllers to load Neural Networks emulators (CNN, RNN / LSTM etc.), thereby creating layers of different types of neurons, thus creating a flexible network architecture.

2. Training Mode "growing axons"

Slide 10. - This mode emulates the establishment of new connections between neurons. "Neuron" system, as usual, are initialized with random values. The input system serves the training data, and the "neurons" are trying to "grow" to the axons of other neurons.

Slide 11. The concrete core - "neuron," "listens" on the bus signals from other packages "neurons" as dendrites receive signals from the axons of neurons. Neural network algorithm in the kernel information accumulates and stores any packets with any address (signals from which "neurons") came.

Slide 12. When a particular "neuron" obtained from "switched" neuron data, it do:
1. Pending the release of the transmission line Transfer / Busy and takes it,
2. Sends from its broadcast packet address (all "neurons") with the calculated value (or simply "1"),
3. Releases Transfer / Busy line
4. Other neurons receive these packets and storing the source address and the value and begin to process the signal of his neural network (see. Prev. Slide)
Thus, the "neurons" are trying to establish a connection, "all with all" - "sprout axons" to each other. To optimize the work area to establish connections can be restricted "layers", "domains", applying a mask on the addressing of packets.

3. The back-propagation mode errors.

Slide 13. When the direct teaching mode is switched feedback error mode (Back propagation line is ON). In this mode, the output value of the entire system serves the training sample.

Slide 14. Backpropagation implemented as a comparison of their data on the output received from the teaching of values. Accordingly, the neural network in a particular weight signals kernel counts packets received from other "neurons". Addresses of "neurons" with the greatest mistake "crossed out" are forgotten.

Slide 15. Over "neurons" (from which came the packets signals with the most correct values) sent packages with a corrective value.

Slide 16. Accordingly, the "neurons" that took on the address packet with a reverse fault, repeat the previous step 2 and adjust its own set of "reliable sources".
Thus, there is a network of training and communication are built similarly to the axons, dendrites in natural neural networks - packages of "neurons" that best predict the value of the training sample is obtained greater weight and less likely prediction - smaller. However, if the neuron's experience a "deficit" of information (it is at the inlet is too small to trigger packets), it may "listen" mode (slide 10) to find new sources to provide network flexibility.

4. Operating mode

Slide 17. When working on the network input mode serves the real values ​​and the network itself, classifies the incoming data.

Slide 18. Each "neuron" receives packets from the "neurons", with the largest weight obtained by learning processing and its neural network.

Slide 19. When triggered, "neuron" expects bus release, captures it, sends from his address broadcast packet (or a certain segment of the network, if it is limited to the network mask).
  Thus, after the processing operation of "neurons" of the network region are formed of data packets that can be processed or sent for processing to another part of the neural network.

