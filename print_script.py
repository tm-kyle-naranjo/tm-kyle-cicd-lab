import sys


def main():
    """Main function to run the script."""
    try:
        num_a, num_b = int(sys.argv[1]), int(sys.argv[2])
    except (ValueError, IndexError):
        print("Error: Two integer arguments are required.")
        sys.exit(1)
    
    print(f"num_a: {num_a}")
    print(f"num_b: {num_b}")
    print(f"Sum: {num_a + num_b}")


if __name__ == "__main__":
    main()