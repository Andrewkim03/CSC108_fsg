def record_candies(records: list[list[str]]) -> None:
    """
    Update the candies received by trick-or-treaters contained in the list
    <records>, where each element is a 2-element list containing a 
    trick-or-treaters name, and the number of candies 
    they received.
    
    The function updates the candies in 'candies.txt' by either adding
    new trick-or-treaters or incrementing the candy count of existing ones.
    """
records = [
    ["Optimus Prime", "5"],
    ["Chat GPT", "3"],
    ["John Doe", "2"],
    ["Lamar Jackson", "4"]
    ["Harry Potter", "4"]
    ["Tony Stark", "10"]
]

record_candies(records)