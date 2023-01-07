import unittest
import numpy as np
import time
from operator import itemgetter

def create_list_norepeated_by_field(list_obj_original=[], find_key=None):
	return list(set([obj.get(find_key) for obj in list_obj_original]))

def sum_customer_and_remove_used_object_from_list(count_customer=None, customers=None, obj_customer=None):
	count_customer += 1
	customers.remove(obj_customer)
	return count_customer

def customer_success_balancing(customer_success=[], customers=[], away_customer_success=[]):
	id_customer_success_max_customer_or_number_tie = None

	if customer_success and customers:
		list_score_norepeated_customer_success = create_list_norepeated_by_field(list_obj_original=customer_success, find_key='score')
		list_score_norepeated_customer = create_list_norepeated_by_field(list_obj_original=customers, find_key='score')

		if len(customer_success) != len(list_score_norepeated_customer_success):
			raise Exception('Equal levels (score) Css were found!')

		if len(customer_success) > 1000:
			raise Exception('Css number cannot be greater than 1000!')

		if len(customers) > 1000000:
			raise Exception('Customers number cannot be greater than 1000000!')

		if any(score > 10000 for score in list_score_norepeated_customer_success):
			raise Exception('Css score cannot be greater than 10000!')

		if any(score > 100000 for score in list_score_norepeated_customer):
			raise Exception('Customers score cannot be greater than 100000!')

		number_of_abstentions = int((len(customer_success) / 2) // 1 or 0)

		if len(away_customer_success) > number_of_abstentions:
			raise Exception('Exceeded maximum abstention limit!')

		customer_success_filtered_away = [css for css in customer_success if css.get('id') not in away_customer_success]

		sorted_customer_success = sorted(customer_success_filtered_away, key=itemgetter('score'))

		for index, customer_success in enumerate(sorted_customer_success):
			score_customer_success = customer_success.get('score')

			count_customer = 0
			#Iteração sobre a cópia da lista para remoção de item conforme condição
			for customer in customers[:]:
				score_customer = customer.get('score')

				if index == 0:
					if score_customer <= score_customer_success:
						count_customer = sum_customer_and_remove_used_object_from_list(count_customer=count_customer, customers=customers, obj_customer=customer)

				else:
					if score_customer > sorted_customer_success[index - 1].get('score') and score_customer <= score_customer_success:
						count_customer = sum_customer_and_remove_used_object_from_list(count_customer=count_customer, customers=customers, obj_customer=customer)

			customer_success['count_customer'] = count_customer

		max_count_customer = max(sorted_customer_success, key=itemgetter('count_customer'))

		id_customer_success_max_customer_or_number_tie = max_count_customer.get('id')

		result_exists_other_max_count_customer = [css for css in sorted_customer_success if css.get('count_customer') == max_count_customer.get('count_customer')
																						and css.get('id') != id_customer_success_max_customer_or_number_tie]

		if result_exists_other_max_count_customer:
			id_customer_success_max_customer_or_number_tie = 0

	return id_customer_success_max_customer_or_number_tie

def build_scores(list_score=[]):
	return [{'id': index + 1 , 'score': score } for index, score in enumerate(list_score)]

class Testing(unittest.TestCase):
	def test_scenario_one(self):
		balancer = customer_success_balancing(customer_success=build_scores([60, 20, 95, 75]),
											customers=build_scores([90, 20, 70, 40, 60, 10]),
											away_customer_success=[2, 4])
		self.assertEqual(balancer, 1)

	def test_scenario_two(self):
		balancer = customer_success_balancing(customer_success=build_scores([11, 21, 31, 3, 4, 5]),
											customers=build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
											away_customer_success=[])
		self.assertEqual(balancer, 0)

	def test_scenario_three(self):
		test_timeout_in_ms = 100
		test_start_time = time.time()
		balancer = customer_success_balancing(customer_success=build_scores(list(range(1, 1000))),
											customers=build_scores(np.full(10000, 998)),
											away_customer_success=[999])
		self.assertEqual(balancer, 998)

		if time.time() - test_start_time > test_timeout_in_ms:
			raise Exception('Test took longer than {}ms!'.format(test_timeout_in_ms))

	def test_scenario_four(self):
		balancer = customer_success_balancing(customer_success=build_scores([1, 2, 3, 4, 5, 6]),
											customers=build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
											away_customer_success=[])
		self.assertEqual(balancer, 0)

	def test_scenario_five(self):
		balancer = customer_success_balancing(customer_success=build_scores([100, 2, 3, 6, 4, 5]),
											customers=build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
											away_customer_success=[])
		self.assertEqual(balancer, 1)

	def test_scenario_six(self):
		balancer = customer_success_balancing(customer_success=build_scores([100, 99, 88, 3, 4, 5]),
											customers=build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
											away_customer_success=[1, 3, 2])
		self.assertEqual(balancer, 0)

	def test_scenario_seven(self):
		balancer = customer_success_balancing(customer_success=build_scores([100, 99, 88, 3, 4, 5]),
											customers=build_scores([10, 10, 10, 20, 20, 30, 30, 30, 20, 60]),
											away_customer_success=[4, 5, 6])
		self.assertEqual(balancer, 3)

if __name__ == '__main__':
	unittest.main()