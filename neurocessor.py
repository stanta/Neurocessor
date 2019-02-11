class Neurocessor:

    teach_mode_flag = True
    back_propagation = False
    neuro_map = [] # map of neuron addresses
    neuro_types = ("RELU", "RNN", "LSTM") # ..., etc...

    def neuron (self_address):

        growing_axons_mode = True
        dendrits = []
        out_axon = False
        current_neuro_type = "RELU" # for example
        answers =[]
        def RELU ():
            # implements RELU
        
        

        # todo memoryview
        if (teach_mode_flag) :
            if growing_axons_mode:
                # "dendrits" looking for new "axons"
            if back_propagation:
                #back propagate mode
        else:
            for dendrit in dendrits:
                # call every dendrit
                answers[] = neuron (dendrit)
                # call think 
                return think(answers, current_neuro_type)
                
            
