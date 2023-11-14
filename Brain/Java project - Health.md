# 계획서
### **사용자 정보 클래스**
키, 몸무게, 성별
체중 감량 또는 증량

### **탄단지 비율 구성**
식이 선호도에 대한 사용자 입력
탄수화물, 단백질, 지방 등의 매크로 영양소 필요량 계산 알고리즘

### **운동 메뉴**
유산소 (심폐 운동)
무산소 (근력 트레이닝: 등, 어깨, 가슴, 하체)
운동 유형과 시간에 기반한 칼로리 계산

### **운동 강도 및 추천 중량**
운동 강도를 제안하는 알고리즘
사용자의 힘 수준에 기반한 근력 트레이닝을 위한 추천 중량

### **루틴 추천**
운동 루틴 생성
사용자의 진행 상황 및 피드백에 맞춰 루틴 조정



# 클래스 설계
1. **User 클래스**
- 속성: 이름, 키, 몸무게, 성별, 목표 무게,  DailyInfo 리스트
- 메서드:
	- 사용자 데이터 입력 (inputUserData)
	- 사용자 목표 설정 (setUserGoals) - 체중 감량, 증량 선택

2. **Nutrition 클래스**
- 속성:
	- 탄수화물 비율 (CarbRatio)
	- 단백질 비율 (ProteinRatio)
	- 지방 비율 (FatRatio)
- 메서드:
	- 매크로 비율 계산 (calculateMacros)
	- 사용자 식이 선호 입력 (inputDietPreferences)

3. **ExerciseMenu 클래스**
- 속성:
	- 유산소 운동 목록 (AerobicList)
	- 무산소 운동 목록 (AnaerobicList)
	- 운동 세부 종목 (ExerciseDetails)
- 메서드:
	- 운동 메뉴 생성 (createExerciseMenu)
	- 칼로리 소모 계산 (calculateCaloriesBurned)

4. **Intensity 클래스**
- 속성:
	- 운동 강도 (IntensityLevel)
	- 추천 중량 (RecommendedWeight)
- 메서드:
	- 운동 강도 결정 (determineIntensity)
	- 중량 추천 (recommendWeight)

5. **Routine 클래스**
- 속성:
	- 운동 루틴 (Routine)
- 메서드:
	- 루틴 추천 (recommendRoutine)
	- 사용자의 피드백에 따른 루틴 수정 (modifyRoutineBasedOnFeedback)

6. **Main 클래스**
- 메인 메소드에서 모든 클래스 인스턴스화
- 사용자 인터페이스 및 흐름 관리