# Neural Style Transfer Project

## Overview
This project focuses on implementing neural style transfer using TensorFlow, particularly using the VGG19 model to merge the style of one image with the content of another.

## Tasks

### Task 0: Initialize
- **Objective:** Initialize the NST class that handles neural style transfer.
- **Features:**
  - Set up public class attributes for style and content layers.
  - Construct the class with initial style and content images, weights for content and style costs.
  - Define and implement a method to scale images appropriately.

### Task 1: Load the Model
- **Objective:** Load the VGG19 model and customize it for neural style transfer.
- **Details:**
  - Modify the class to include a method that loads the VGG19 model.
  - Configure the model inputs and outputs based on style and content features.

### Task 2: Gram Matrix
- **Objective:** Implement a static method to calculate the Gram matrix of a layer.
- **Functionality:**
  - The method should compute the Gram matrix for assessing the style of an image.

### Task 3: Extract Features
- **Objective:** Extract features necessary for calculating the style and content costs.
- **Implementation:**
  - Update the class to extract style and content features from their respective layers.

### Task 4: Layer Style Cost
- **Objective:** Calculate the style cost for a single layer.
- **Approach:**
  - Define a method that computes the style cost between a generated style output and a target style gram matrix.

### Task 5: Style Cost
- **Objective:** Calculate the overall style cost from multiple layers.
- **Method:**
  - Implement a function that accumulates style costs from all specified layers, adjusting for their relative weights.

### Task 6: Content Cost
- **Objective:** Define a method to compute the content cost between the generated and content images.
- **Functionality:**
  - The method should evaluate how different the content of the generated image is from the original content image.

### Task 7: Total Cost
- **Objective:** Calculate the total cost combining style and content costs.
- **Details:**
  - Implement a method that computes the total cost as a weighted sum of content and style costs.

### Task 8: Compute Gradients
- **Objective:** Calculate gradients of the total cost with respect to the generated image.
- **Features:**
  - Develop a method to compute these gradients, which are necessary for the gradient descent optimization algorithm.

### Task 9: Generate Image
- **Objective:** Use gradient descent to iteratively update the generated image towards the style target.
- **Process:**
  - Implement a method that performs iterations of updates on the image, printing costs at specified intervals.

### Task 10: Variational Cost
- **Objective:** Introduce a variational cost to smooth the generated image.
- **Extension:**
  - Update the total cost calculation to include a term that penalizes large variations in adjacent pixel values.

## Conclusion
Each task progressively builds on the last, creating a system that can apply the style of famous paintings or any image to the content of another photograph or image. 
