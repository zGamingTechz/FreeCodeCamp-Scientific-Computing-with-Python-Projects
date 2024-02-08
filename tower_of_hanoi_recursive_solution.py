# Set the number of disks
NUMBER_OF_DISKS = 5

# Initialize the rods with the starting configuration
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Source rod
B = []  # Auxiliary rod
C = []  # Target rod

def move(n, source, auxiliary, target):
    """
    Recursive function to solve the Tower of Hanoi puzzle.

    Parameters:
    - n: The number of disks to move.
    - source: The source rod from which to move the disks.
    - auxiliary: The auxiliary rod to use during the move.
    - target: The target rod to which the disks should be moved.
    """
    # Base case: If there are no disks to move, return
    if n <= 0:
        return
    
    # Move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # Move the nth disk from source to target
    target.append(source.pop())
    
    # Display the current state of rods A, B, and C
    print("Rods: A =", A, "B =", B, "C =", C, '\n')
    
    # Move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)

# Initiate the call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
