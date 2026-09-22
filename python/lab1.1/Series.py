class SeriesCalculator:

    @staticmethod
    def sum_finite(term_func, start, end):
       
        return sum(term_func(k) for k in range(start, end + 1))


    @staticmethod
    def sum_infinite(term_func, start=0, eps=1e-9, max_iter=10**7):

        s = 0.0
        terms = 0
        
        for k in range(start, max_iter):
            term = term_func(k)
            if abs(term) < eps:
                break
            s += term
            terms += 1
            
        return s, terms 
    
    @staticmethod
    def series_sum_with_tolerance_infinite(term_func, epsilon=10**-9, max_iter=10**7):
        
        s = 0.0 

        for n in range(1, max_iter + 1):
            term = term_func(n)
            s += term 

            if abs(term) < epsilon:
                return s, n

        return s, max_iter  
    
    @staticmethod
    def series_sum_with_tolerance(term_func, epsilon=1e-6, max_iter=100000):
        s = 0.0
        prev_s = 0.0 

        for n in range(1, max_iter + 1):
            s += term_func(n)

            if abs(s - prev_s) / (abs(s) + 1e-12) < epsilon:
                return s, n

            prev_s = s

        return s, max_iter  # якщо не зійшлося, повертаємо максимум