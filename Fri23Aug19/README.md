## Motivation
To understand how to do basic data analysis calculations, and the implications on compute resources

## Scenario
Your manager tells you about this new dataset and asks you to calculate few metrics from it.
the metrics needed will have to be re-calculated on a very frequent basis
Dataset is simple, and contains four columns of decimal numbers (assume they are salaries or other dollar figures, so you need to be accurate and cannot afford approximations).
he is interested in only one column (say 3rd column) and requires you to calculate the following metrics:
+ Sample Mean in decimal for col3 .. check wiki for formula
+ Sample Standard Deviation in decimal for col3 .. check wiki for formula
+ Max of col3 .. 
+ Min of col3 .. 

As stated above, really simple calculations, so you as a seasoned data analyst/scientist/guru should be able to do this quickly and efficiently.

One caveat, dataset and corresponding csv file happen to be several Gigabytes in size, 16 Gigabytes in this case, and although it is not even close to being called big data, assume that future datasets might grow significantly on the exact day you convince your manager that more hardware would solve the problem (i.e. assume dataset will always be multple times the size of your computer/server available memory)
Also, your boss needs the results as soon as possible, as decision will need to be made, and new data will be available very soon.


## Tooling
bring your best tools, no judgement! as long as the tool does the job.
Fancy using R and dplyr? python3, numpy and pandas? SQL and stored procedures? Bash and awk? Matlab and Mathematica? Excel and access? Abacus?
Feel free to do so! your boss only cares for accurate and timely results.

## Sanity Check
The solution you develop should run fast (boss standing on your desk waiting, unless u like them standing there) and use reasonable amount of resources (should be able to run on your 5 year old laptop) while returning the correct results.

## how to genrate the said dataset
+ git clone this library into your $GOPATH
+ go run main.go
+ this might take around 20minutes..go have your coffee and think about your attack strategy
+ the dataset csv file will be genrated next to the main.go file
+ it will be reasonably sized (~16GB) so make sure you have enough disk space
+ run wc -l *.csv and you should get 4x10^8 rows plus the header.
+ your dataset is now availble and you should theoritically be able to find the answers.
+ try not to cheat by reverse engineering the code that generates the dataset, assume data was generated organically rather than synthetically, and that code do not exit.
