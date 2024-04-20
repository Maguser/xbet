!pip install numpy==1.21.6
import streamlit as st
import math
import pandas as pd
import numpy as np

st.title("Критерий Келли")
st.subheader("Используем это приложение Streamlit, чтобы рассчитать "
"размер ставки по критерию Келли")

# Критерий Келли
def C_c ():
    koef = st.number_input(label = "Ввести коэффициент букмекера")
    B = st.number_input(label = "Ввести расчитанный процент уверенности", min_value=0.0, max_value=1.0, value = .5)
    bank = st.number_input(label = "Ввести размер банка")
    print('Размер ставки')
    percent =  (koef * B - 1) / (koef - 1)
    return round(percent * bank, 0)

st.write("Размер ставки:", C_c())

st.subheader("Используем для принятия решения, ставки на футбол ")

def what_bet():
    h = st.number_input(label = "Введите честный коэф хозяев(фаворита) ", value = .5)
    g = st.number_input(label = "Введите честный коэф гостей(аутсайдера) ", value = .5)
    h_ = round((100/h/100),2)
    g_ = round((100/g/100),2)
    delta = round((h_ - g_), 2)
    st.write("Разница", delta)
    if delta > 0.4:
        st.write("Ставить на хозяев")
    elif delta < 0.15:
        st.write("Ставить на ничью")
    else: st.write("Не ставить")
	
what_bet()

st.subheader("Дневник выигрышей/проигрышей ")


if "my_wins" not in st.session_state:
	st.session_state.my_wins = [0]
	
st.write("Мои текущие выигрыши/проигрыши:", st.session_state.my_wins)

new_todo = st.number_input("Что нужно еще добавить?")

if st.button("Добавить новый выигрыш/проигрыш"):
	st.write("Добавление нового элемента в список")
	st.session_state.my_wins.append(new_todo)
st.session_state.my_wins.append(new_todo)

# дописать дневник на кого ставить Лайал - Ли.Д 1,32 - 2,99 предлагают П2 мой коэф уверенности 0,55 банк 10000
# в этой реализации с новым запуском,предыдущее состояние пропадает
