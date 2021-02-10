"""
The Postal department of a country X, issues stamps. The denomination values of the stamps issued are in the respective
currency value of 1, 2, 5, 10, 50 and 100 of the country X.
Also each of the stamps can be issued in three different shapes which are Square Shape, Rectangle Shape
and Triangular Shape.
Plus, the country X has got 100 prominent National leaders and each of the stamp has got the face of one of the
national leader embossed in it. A very curious stamp collector wants to create a collection, which contains all the
different possible stamps issued by the country X.
 The stamp collector is able to collect one stamp at a time from the posts he receives, with each stamp being equally
 likely to show up on the post/envelope.
a. What is the expected number of Stamps required to be collected by the hobbyist so that he has a full collection?
b. How will you change your solution, if in the future the country adds more prominent National leaders to emboss list?
"""


def possible_stamp_collections(denomination_values: list, stamp_shape: list, number_of_leaders: int):

    number_of_notes = len(denomination_values)
    number_of_shapes = len(stamp_shape)

   """Assuming each stamp can have all the shapes and all the leaders """
    possible_outcomes = number_of_leaders * number_of_notes * number_of_shapes
    print(f'No of possible outcomes {possible_outcomes}')

    number_of_tickets_to_be_collected = possible_outcomes * harmonic_mean_outcomes(possible_outcomes)
    print(f'Total number of tickets to be collected by the hobbyist are {number_of_tickets_to_be_collected}')


def harmonic_mean_outcomes(n):
    # H1 = 1
    harmonic_mean = 1

    for i in range(2, n):
        harmonic_mean += 1/i

    return harmonic_mean


if __name__ == "__main__":
    denomination_values = [1, 2, 5, 10, 50, 100]
    stamp_shapes = ['square', 'rectangle', 'triangle']
    number_of_leaders = 100
    possible_stamp_collections(denomination_values, stamp_shapes, number_of_leaders)

