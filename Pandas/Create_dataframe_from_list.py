import pandas as pd
from typing import List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    col_names = ["student_id", "age"]
    df = pd.DataFrame(student_data, columns = col_names)
    return df