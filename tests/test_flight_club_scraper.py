from prompt.flight_club_scraper import capture_results_into_list_of_5,create_index_list,create_chosen_list,display_out_of_stock

def test_capture_results():
  actual = capture_results_into_list_of_5([8,9,10,11,12,13,14,15])
  expected = [8,9,10,11,12]
  assert actual == expected

def test_capture_less_than_5():
  actual = capture_results_into_list_of_5([8,9])
  expected = [8,9]
  assert actual == expected

def test_create_index_list_1():
  actual = create_index_list('3')
  expected = [3]
  assert actual == expected

def test_create_index_list_2():
  actual = create_index_list('23')
  expected = [2,3]
  assert actual == expected

def test_create_chosen_list():
  actual = create_chosen_list([3,2,1,0,4],[0])
  expected = [3]

def test_display_out_of_stock():
  actual = display_out_of_stock()
  expected = "display_out_of_stock"

#def test_