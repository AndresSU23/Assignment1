import cv2
import numpy as np
import math

# Create a blank white image
width, height = 500, 500
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Ellipse parameters
# Circle parameters
radius = 90
center = (width // 2, height // 2)
offset_x = 100
offset_y = 90

# Define new positions
positions = {
    "red":    (center[0], center[1] - offset_y),              # Top center
    "green":   (center[0] - offset_x, center[1] + offset_y),   # Bottom-left
    "blue":  (center[0] + offset_x, center[1] + offset_y),   # Bottom-right
}

# Draw the circles
cv2.circle(image, positions["red"], radius, (0, 0, 255), -1)    # Red
cv2.circle(image, positions["blue"], radius, (255, 0, 0), -1)   # Blue
cv2.circle(image, positions["green"], radius, (0, 255, 0), -1)  # Green

cv2.circle(image, positions["red"], radius//2, (255, 255, 255), -1)     # Blue
cv2.circle(image, positions["blue"], radius//2, (255, 255, 255), -1)     # Green
cv2.circle(image, positions["green"], radius//2, (255, 255, 255), -1)     # Red

def draw_trapezium(image, center, direction, bottom_base=80, top_base=20, height=90, color=(255, 255, 255), thickness=-1):
    cx, cy = center
    angle_rad = math.radians(direction)

    # Direction vector (along height)
    dx = math.cos(angle_rad)
    dy = -math.sin(angle_rad)  # y-axis goes down in images

    # Perpendicular vector (to spread the width)
    px = -dy
    py = dx

    # Top base (shorter) is at the center
    p1 = (cx - px * top_base / 2, cy - py * top_base / 2)
    p2 = (cx + px * top_base / 2, cy + py * top_base / 2)

    # Bottom base (wider) is height away in the given direction
    far_x = cx + dx * height
    far_y = cy + dy * height
    p3 = (far_x + px * bottom_base / 2, far_y + py * bottom_base / 2)
    p4 = (far_x - px * bottom_base / 2, far_y - py * bottom_base / 2)

    # Convert to points array
    pts = np.array([p1, p2, p3, p4], dtype=np.int32).reshape((-1, 1, 2))

    # Draw filled trapezium
    cv2.fillPoly(image, [pts], color, lineType=cv2.LINE_AA)

# Draw trapeziums
draw_trapezium(image, positions["red"], direction=270)         # Pointing down
draw_trapezium(image, positions["blue"], direction=90)       # Pointing up
draw_trapezium(image, positions["green"], direction=45)      # Pointing top-right


# Add text "OpenCV"
font = cv2.FONT_HERSHEY_SIMPLEX
text = "OpenCV"
font_scale = 1
thickness = 2
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
text_x = (width - text_size[0]) // 2
text_y = height - 20
cv2.putText(image, text, (text_x, text_y), font, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)

# Display the image
cv2.imshow("OpenCV Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
