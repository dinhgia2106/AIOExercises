import numpy as np
import cv2

# Load and resize images
bg1_image = cv2.imread('GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    # Convert the images to grayscale
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = cv2.cvtColor(
        difference_single_channel, cv2.COLOR_BGR2GRAY)

    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    # Apply a binary threshold to get a binary mask
    _, difference_binary = cv2.threshold(
        difference_single_channel, 50, 255, cv2.THRESH_BINARY)

    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    # Compute the difference to obtain the mask
    difference_single_channel = compute_difference(bg1_image, ob_image)

    # Compute the binary mask
    binary_mask = compute_binary_mask(difference_single_channel)

    # Replace the background using the mask
    output = np.where(binary_mask[:, :, None] == 255, ob_image, bg2_image)

    return output


# Replace background
final_output = replace_background(bg1_image, bg2_image, ob_image)

# Display the final output
cv2.imshow(final_output)
