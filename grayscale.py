import cv2
import os

print("1. Convert image to grayscale")
print("2. Delete an image file")
print("3. Exit")

try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("Invalid input.")
    exit()

if choice == 1:
    image_name = input("Enter image file name (with extension): ")

    # Read the image
    image = cv2.imread(image_name)

    if image is None:
        print("Error: Image not found or unsupported format.")
    else:
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Display images
        cv2.imshow("Original Image", image)
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save option
        save = input("Do you want to save the grayscale image? (y/n): ")

        if save.lower() == 'y':
            output_name = input("Enter output file name (with extension): ")

            if output_name.strip() == "":
                output_name = "grayscale_output.jpg"

            cv2.imwrite(output_name, gray)
            print("Image saved successfully!")
        else:
            print("Image not saved.")
    pass

elif choice == 2:
    file_name = input("Enter file name to delete (with extensions) : ")

    if os.path.exists(file_name):
        confirm = input("Are you sure you want to delete this file? (y/n): ")
        if confirm.lower() == 'y':
            os.remove(file_name)
            print("File deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("File not found.")

elif choice == 3:
    print("Exiting program.")

else:
    print("Invalid choice.")
