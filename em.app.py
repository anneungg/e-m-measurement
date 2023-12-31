import math
import streamlit as st

# 실험에서 사용되는 이론값
theoretical_value = 1.758820024e11  # 전자의 비전하량 이론값 (C/kg)

# 기능: 사용자 입력 값을 바탕으로 계산 수행
def calculate_properties(V, I_H, R, r, V_H, N):
    if R == 0:
        return "코일의 반경 값은 0보다 커야 합니다."
    
    M0 = 4 * math.pi * 1e-7  

    B = 0.176 * M0 * N * I_H / R  
    e_over_m = 2 * V * 125 * R ** 2 / ((8 * M0 * N * I_H) ** 2 * r ** 2)  

    return {
        "I_H": I_H,
        "V_H": V_H,
        "B": B,
        "e_over_m": e_over_m
    }

# 기능: Streamlit을 사용하여 사용자 인터페이스 제공
def main():
    st.title("e/m(비전하량) 계산기")

    V = st.number_input("가속전압 (V)을 입력하세요:", value=0.0)
    I_H = st.number_input("헬름홀츠 코일에 걸린 전류 (A)를 입력하세요:", value=0.0)
    R = st.number_input("코일의 반경 (mm)을 입력하세요:", value=0.0)
    r = st.number_input("전자의 원형 궤도 반지름 값 (mm)을 입력하세요:", value=0.0)
    V_H = st.number_input("헬름홀츠 코일에 걸린 전압 (V)를 입력하세요:", value=0.0)
    N = st.number_input("헬름홀츠 코일의 감긴 수(N)을 입력하세요(코일 2개면):", value=0.0)

    if st.button("계산하기"):
        result = calculate_properties(V, I_H, R, r, V_H, N)
        if isinstance(result, str):
            st.error(result)
        else:
            st.write("### 계산 결과")
            st.write(f"헬름홀츠 코일에 걸린 전류 (I_H): {result['I_H']} A")
            st.write(f"헬름홀츠 코일의 전압 (V_H): {result['V_H']} V")
            st.write(f"자기장 (B): {result['B']} T")
            st.write(f"e/m (전자의 비전하량): {result['e_over_m']} C/kg")

            # 이론값과 비교하여 오차율 계산
            error_percentage = abs(result['e_over_m'] - theoretical_value) / theoretical_value * 100
            st.write(f"오차율: {error_percentage:.2f}%")
if st.button("app.py 코드 보기"):
    code = '''
import math
import streamlit as st

# 실험에서 사용되는 이론값
theoretical_value = 1.758820024e11  # 전자의 비전하량 이론값 (C/kg)

# 기능: 사용자 입력 값을 바탕으로 계산 수행
def calculate_properties(V, I_H, R, r, V_H, N):
    if R == 0:
        return "코일의 반경 값은 0보다 커야 합니다."
    
    M0 = 4 * math.pi * 1e-7  

    B = 0.176 * M0 * N * I_H / R  
    e_over_m = 2 * V * 125 * R ** 2 / ((8 * M0 * N * I_H) ** 2 * r ** 2)  

    return {
        "I_H": I_H,
        "V_H": V_H,
        "B": B,
        "e_over_m": e_over_m
    }

# 기능: Streamlit을 사용하여 사용자 인터페이스 제공
def main():
    st.title("e/m(비전하량) 계산기")

    V = st.number_input("가속전압 (V)을 입력하세요:", value=0.0)
    I_H = st.number_input("헬름홀츠 코일에 걸린 전류 (A)를 입력하세요:", value=0.0)
    R = st.number_input("코일의 반경 (mm)을 입력하세요:", value=0.0)
    r = st.number_input("전자의 원형 궤도 반지름 값 (mm)을 입력하세요:", value=0.0)
    V_H = st.number_input("헬름홀츠 코일에 걸린 전압 (V)를 입력하세요:", value=0.0)
    N = st.number_input("헬름홀츠 코일의 감긴 수(N)을 입력하세요(코일 2개면):", value=0.0)

    if st.button("계산하기"):
        result = calculate_properties(V, I_H, R, r, V_H, N)
        if isinstance(result, str):
            st.error(result)
        else:
            st.write("### 계산 결과")
            st.write(f"헬름홀츠 코일에 걸린 전류 (I_H): {result['I_H']} A")
            st.write(f"헬름홀츠 코일의 전압 (V_H): {result['V_H']} V")
            st.write(f"자기장 (B): {result['B']} T")
            st.write(f"e/m (전자의 비전하량): {result['e_over_m']} C/kg")

            # 이론값과 비교하여 오차율 계산
            error_percentage = abs(result['e_over_m'] - theoretical_value) / theoretical_value * 100
            st.write(f"오차율: {error_percentage:.4f}%")

if __name__ == "__main__":
    main()

    '''
    st.code(code, language="python")
    
if __name__ == "__main__":
    main()
