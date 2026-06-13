class Perceptron : 
    def __init__(self , weights , bias):
        self.weights = weights 
        self.bias = bias
        
    def predict(self , inputs):
        linear_output = sum(w * x for w , x in zip(self.weights , inputs , strict=True)) + self.bias 
        prediction = 1 if linear_output >= 0 else 0
        return prediction 
    

#Example Usage 
weights = [float(x) for x in input("Enter the weights (comma separated) : ").split(",")]
bias = float(input("Enter the bias : "))

perceptron = Perceptron(weights , bias)
inputs = [float(x) for x in input("Enter the inputs (comma separated) : ").split(",")]
output = perceptron.predict(inputs)
print(f"Predicted Output : {output}")