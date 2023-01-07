import argparse
import math

def differentiate_payment(principal, interest, periods, month_number):
    interest = (float(interest) / (100 * 12))
    principal = int(principal)
    periods = int(periods)
    d = (principal / periods) + interest * (principal - ((principal * ((m - 1) / periods))))
    return math.ceil(d)


def annuity_payment(principal, periods, interest):
    interest = (float(interest) / (100 * 12))
    principal = int(principal)
    periods = int(periods)
    a = principal * (interest * ((1 + interest)**periods) / (((1 + interest)**periods)- 1))
    return math.ceil(a)

def loan_principal(payment, periods, interest):
    interest = (float(interest) / (100 * 12))
    payment = int(payment)
    periods = int(periods)
    p = payment / ((interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))
    return math.floor(p)

def payment_periods(principal, payment, interest):
    interest = (float(interest) / (100 * 12))
    payment = int(payment)
    principal = int(principal)
    n = math.log(((payment) / (payment - (interest * principal))), 1 + interest)
    return math.ceil(n)


parser = argparse.ArgumentParser(description="this is a loan calculator")
parser.add_argument("--type", help="choose between diff and annuity")
parser.add_argument("--payment", help="type the payment amount")
parser.add_argument("--principal", help="type the principal amount")
parser.add_argument("--periods", help="type the periods in months")
parser.add_argument("--interest", help="type the interest rate")
args = parser.parse_args()

arg_list = [args.type, args.payment, args.principal, args.periods, args.interest]
arg_list_none = []
for item in arg_list:
    if item != None:
        arg_list_none.append(item)
if len(arg_list_none) < 4:
    print("Incorrect parameters")

elif args.type not in ["diff", "annuity"]:
    print("Incorrect parameters")

elif (args.payment is not None) and (args.type == "diff"):
    print("Incorrect parameters")

elif (args.interest is None):
    print("Incorrect parameters")

elif args.type == "diff":
    m = 0
    total_paid = 0
    for month_number in range(int(args.periods)):
        m += 1
        d = differentiate_payment(args.principal, args.interest, args.periods, m)
        print("Month %s: payment is %s" % (m, d))
        total_paid += d
    over_payment = total_paid - int(args.principal)
    print("Overpayment = %s" % (over_payment))

elif args.type == "annuity":
    if args.payment is None:
        annuity = annuity_payment(args.principal, args.periods, args.interest)
        print("Your annuity payment = %s!" % (annuity))
        over_payment = (annuity * int(args.periods)) - int(args.principal)
        print("Overpayment = %s" % (over_payment))
    elif args.principal is None:
        principal_loan = loan_principal(args.payment, args.periods, args.interest)
        print("Your loan principal = %s!" % (principal_loan))
        over_payment = (int(args.payment) * int(args.periods)) - principal_loan
        print("Overpayment = %s" % (over_payment))
    elif args.periods is None:
        periods_payment = payment_periods(args.principal, args.payment, args.interest)
        if periods_payment == 1:
            print("It will take 1 month to repay this loan!")
        elif (periods_payment > 1) and (periods_payment < 12):
            print("It will take %s months to repay this loan!" % (periods_payment))
        elif periods_payment == 12:
            print("It will take 1 year to repay this loan!")
        elif (periods_payment > 12) and (periods_payment % 12 == 0):
            print("It will take %s years to repay this loan!" % (int(periods_payment / 12)))
        elif periods_payment > 12 and periods_payment % 12 == 1:
            print("It will take %s years and 1 month to repay this loan!" % (int(math.floor(periods_payment / 12))))
        elif periods_payment > 12 and periods_payment % 12 > 1:
            print("It will take %s years and %s months to repay this loan!" % (int(math.floor(periods_payment / 12)), (periods_payment % 12)))
        over_payment = (int(args.payment) * int(periods_payment)) - int(args.principal)
        print("Overpayment = %s" % (over_payment))