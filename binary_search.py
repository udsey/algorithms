import random


def check_guess(guess, n):
    if guess > n:
        return 'less'
    elif guess < n:
        return 'more'
    else:
        return 'gotcha!'

def calc_guess(in_range):
    return int(sum(in_range)/2)

def guess_number(n, in_range):    
	guess = calc_guess(in_range)
	i = 1
	while True:
		if check_guess(guess, n) == 'less':
		    in_range[1] = guess
		elif check_guess(guess, n) == 'more':
		    in_range[0] = guess
		else:
		    print(f'Number is {guess}, founded for {i} iterations')
		    break
		guess = calc_guess(in_range)
		i += 1
		
if __name__ == "__main__":

	in_range = []
	in_range.append(int(input('Enter lower bound (int):')))
	in_range.append(int(input('Enter upper bound (int):')))
	n = random.randint(in_range[0], in_range[1])
	print(f'Number to guess is {n}')
	guess_number(n, in_range)
