with open("ticket_concert_artists.csv", "r") as input:
    with open("ticket_concert_artists_2.csv", "w") as output:
        for row in input:
            if row[0] == '"':
                output.write(row.rstrip()[1:-1])
            else:
                output.write(row.rstrip() + '\n')
