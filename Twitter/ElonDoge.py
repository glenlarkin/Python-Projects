import twint

# Configure
c = twint.Config()
c.Username = "elonmusk"
c.Search = "DOGE"

# Run
twint.run.Search(c)