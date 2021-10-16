import di
import pandas_datareader.data as wb

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibWFydmluIiwiYXVkIjoibWFydmluIiwiZXhwIjoxNjM0MzU5MDYzLCJqdGkiOiI2NzY3M2QwZS01ODEyLTRhOWUtOWYxNi1iMjc5MjgxZDJkMmIiLCJpYXQiOjE2MzQzNTU0NjMsImlzcyI6IjQyREkuQ09NIiwic3ViIjoiQVBJIn0.xFXDlnoxUCXn4nqf98-4k6RbgXciMATO9zd3KuvfHts"

#humans = wb.DataReader('POP_FIVE_HIST', 'oecd')
#di.put("42di.cn/marvin/tutorials/humans", humans, token, update_schema=True)

humans = di.read("42di.cn/marvin/tutorials/humans", token)
print(humans.head(10))