import numpy as np

def function(x1,x2,x3): 
    # Define the x and y coordinates of your points
    x = np.array([-6, 5.4, -5, -3, 2.1, -1, 0 , 1, 1.5,2.5,3])
    y = np.array([0, 0, 0, 0, 0, 0, 0 , 0, 0,0,0])

    # Fit a polynomial of degree n to the data (n is the degree of the polynomial)
    n = 3  # You can adjust the degree as needed
    coefficients = np.polyfit(x, y, n)

    # Create a polynomial function using the coefficients
    poly_function = np.poly1d(coefficients)

    # You can now evaluate the polynomial function at any x value
    x_new = 6
    y_new = poly_function(x_new)

    print(f"The value of the polynomial at x = {x_new} is y = {y_new}")


def main():
    print("main")  
        
    
if __name__ == '__main__':
    main()