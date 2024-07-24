from PIL import Image
import sys

# sys.argv is a list containing all command-line arguments
# sys.argv[0] is always the script name

if len(sys.argv) > 1:
  # Access arguments after the script name
  filename = sys.argv[1]
  print(f"Using file: {filename}")
else:
  print("Error: Please provide a filename as an argument.")

def display_ppm(filename):
  """
  Opens and displays a PPM image using Pillow.

  Args:
      filename: The path to the PPM file.
  """
  try:
    image = Image.open(filename)
    image.show()  # Displays the image using the default viewer
  except FileNotFoundError:
    print(f"Error: File not found: {filename}")
  except Exception as e:
    print(f"Error displaying image: {e}")

display_ppm(filename)
