import pandas as pd

# Quantity
total_card                              = 52
round_game                              = 33

# Price
price_revealed                          = [0,0,0,0]
price_mine                              = [0,0,0,0]

# Define list for row name and column name for pandas dataframe
securities                              = ['clover','diamond','heart','spade']
prices_names                            = ['price revealed','price mine']


################## Calculate price of securities ##################

for i in range(round_game):

    my_card = []
    revealed_card = []

    # Input cards that I have (For Market Makers, Not For Spectators)
    for j in securities:
        my_card_str                     = input(f"what is my {j}: ")
        my_card.append(float(my_card_str))

    # Input cards that are revealed
    for j in securities:
        revealed_card_str               = input(f"revealed {j}: ")
        revealed_card.append(float(revealed_card_str))

    # Calculate price revealed and price that I can find using my cards
    total_revealed                      = total_card - sum(revealed_card)
    total_mine                          = total_revealed - sum(my_card)

    for j in range(4):
        price_revealed[j]               = ((total_card/4 - revealed_card[j]) / total_revealed * 100)
        price_mine[j]                   = ((total_card/4 - revealed_card[j] - my_card[j]) / total_mine * 100)

    # Print the prices
    price                               = [price_revealed,
                                           price_mine]

    df                                  = pd.DataFrame(price,
                                                       columns=securities,
                                                       index=prices_names)
    print(df)

