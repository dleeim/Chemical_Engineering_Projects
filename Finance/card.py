import pandas as pd

# Quantity
total_card                              = 52
round_game                              = 33

# Price
price_revealed                          = [0,0,0,0]
price_mine                              = [0,0,0,0]


################## Calculate price of securities ##################

for i in range(33):
    # Define list for row name and column name for pandas dataframe
    column_names                        = ['clover','diamond','heart','spade']
    row_names                           = ['price revealed','price mine']

    # Input cards that I have not revealed
    my_clover_str                       = input("what is my clover: ")
    my_diamond_str                      = input("what is my diamond: ")
    my_heart_str                        = input("what is my heart: ")
    my_spade_str                        = input("what is my spade: ")
    my_card                             = [float(my_clover_str),float(my_diamond_str),float(my_heart_str),float(my_spade_str)]

    # Input cards that are revealed
    revealed_clover_str                 = input("update new revealed clover: ")
    revealed_diamond_str                = input("update new revealed diamond: ")
    revealed_heart_str                  = input("update new revealed heart: ")
    revealed_spade_str                  = input("update new revealed spade: ")
    revealed                            = [float(revealed_clover_str),float(revealed_diamond_str),float(revealed_heart_str),float(revealed_spade_str)]

    # Calculate price revealed and price that I can find using my cards
    total_revealed                      = total_card - sum(revealed)
    total_mine                          = total_revealed - sum(my_card)

    for j in range(4):
        price_revealed[j]               = ((total_card/4 - revealed[j]) / total_revealed * 100)
        price_mine[j]                   = ((total_card/4 - revealed[j] - my_card[j]) / total_mine * 100)

    # Print the prices
    price                               = [price_revealed,
                                        price_mine]

    df                                  = pd.DataFrame(price,
                                                    columns=column_names,
                                                    index=row_names)
    print(df)

