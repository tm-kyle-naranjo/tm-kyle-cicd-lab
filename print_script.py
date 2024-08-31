import sys


def main():
    """Main function to run the script."""
    try:
        num_a = float(sys.argv[1])
        num_b = float(sys.argv[2])
    except (ValueError, IndexError):
        print("Error: Two numeric arguments are required.")
        sys.exit(1)
    
    print(f"num_a: {num_a}")
    print(f"num_b: {num_b}")
    print(f"sum: {num_a + num_b}")


if __name__ == "__main__":
    main()