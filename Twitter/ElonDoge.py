import twint

# Configure
c = twint.Config()
c.Username = "whale_alert"
c.Search = "DOGE"

# Run
twint.run.Search(c)