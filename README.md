# redirect-checker
Script to check redirects in bulk

# Usage
All you need to have - csv file in format
```
http://url.redirect/from/, https://url.redirect/to
https://url.redirect/from1/, https://url.redirect/to/anything/else
```
After that you can run script like
```
./redirect_checker.py your_file_with_urls.csv result.csv
```
and get result containing your initial data, address actually your url refers to, quantity of redirect and field which indicates is redirect perform as you desired.
