def smallest(results):
    # receives the first result
    smaller = results[0]

    # for each result, check if there is some smaller in length than the first one, if it's, then store it in smaller variable
    for result in results:
        if (len(smaller) > len(result)):
            smaller = result