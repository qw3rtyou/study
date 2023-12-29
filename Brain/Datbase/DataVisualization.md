
# 기본 그래프 종류

line    df.plot(kind='line')
선형 그래프

bar    df.plot(kind='bar',stacked=True)
막대형 그래프

pie    df['KBS'].plot(kind='pie')
원형 그래프

histogram    df.plot(kind='hist',y='Height',bins=20)
마크버전 정규분포

box_plot    df.plot(kind='box',y='Height')
box형태로 25%마다 어딘지 표시+이상한 값 제거

scatter    df.plot(kind='scatter',x='math',y='writing')
점으로 data표현

kde_plot    sns.kdeplot(body_df['Height'],bw=0.01)
비연속적인 그래프를 부드러운 곡선으로 연속적이게

distribution_plot    sns.distplot(body_df['Height'],bins=15)
정규분포+막대그래프

vilolin_plot    sns.violinplot(x=body_df['Height'])
바이올린처럼 생긴 box_plot 시각적으로 이쁨

등고선    sns.kdeplot(body_df['Height'],body_df['Weight'])
등고선처럼 생긴 형태 같은 지점에 너무 많은 데이터가 몰려있을 때 용이함
이런 경우 데이터 포인터가 서로 중복된다고 표현하고
이러한 그래프를 입체적이라고 표현한다.

앤스컴 콰르텟..?    sns.lmplot(data=body_df,y='Weight',x='Height')
scatter에 대표하는 선하나

catplot    sns.catplot(data=laptop_df,x='os',y='price',kind='box')
색상(hue)과 행(row) 등을 동시에 사용하여 3 개 이상의 카테고리를 표현        

# 그래프+

stripplot    sns.stripplot(data=titanic, x="Survived", y="Age")
sns.catplot(data=laptop_df,x='os',y='price',kind='strip',hue='processor_brand')
데이터 포인터가 서로 중복되있을 때 산점도으로 보여줌

swarmplot    sns.catplot(data=laptop_df,x='os',y='price',kind='swarm',hue='processor_brand')
데이터 포인터가 서로 중복되있을 때 산점도으로 보여줌

heatmap    sns.heatmap(df.corr())
색을 통해서 얼마나 관련있는지를 표현

jointplot    sns.jointplot(data=basic_info,x='Height',y='Weight')
scatter+bar

pairplot    sns.pairplot(tips)
각각 쌍의 그래프를 보여줌

rugplot    잘모름 추가바람

# PDF(Probability Density Function)
확률 밀도 함수
확률 밀도 함수는 데이터셋의 분포를 나타낸다.
특정 구간의 확률은 그래프 아래 그 구간의 면적과 동일하다.
그래프 아래의 모든 면적을 더하면 1이 된다.

# KDE(Kernel Density Estimation)
실제 세계에서 모을 수 있는 데이터는 연속적이지 않기때문에
부드로운 곡선이 아니라 직선이 나올 수 밖에 없다.
KDE는 실제 분포랑 비슷하게 부드러운 곡선이 나오게 만들어줌

# 상관계수
어떤 두 값이 비례혹은 반비례관계가 있는지 확인하고 싶다면
두 값 사이의 상관계수를 확인해 보면 된다.
df.corr()

# EDA(Exploratory Data Analysis)
탐색적 데이터 분석
데이터셋을 다양한 관점에서 살펴보고 탐색하면서 인사이트를 찾는 것

# 클러스터 분석(Cluster Analysis)
비슷한 성향끼리 그룹화해서 분석 혹은 그룹화하는 것

# 새로운 인사이트 발견하기
비슷해 보이거나 서로 관련있는 것들을 그룹지어서 결과를 내보면
다양한 통찰을 얻을 수 있음

```python
df.sum(axis='columns')
df[df['Genre'].str.contains('Blues')]
df['Genre'].str.startswith('Blues')
address=df['소재지도로명주소'].str.split(pat='-',n=1,expand=True)
df['brand'].map(brand_nation)    #brand_nation=>dict

#groupby
그룹지어서 분석할 때 사용함

nation_groups=df.groupby('brand_nation')
type(nation_groups)

>>pandas.core.groupby.generic.DataFrameGroupBy

nation_groups.count()
nation_groups.max()
nation_groups.mean()
nation_groups.first()
nation_groups.last()
nation_groups.plot(kind='box',y='price')
nation_groups.plot(kind='hist',y='price')

#평균함수(mean())이용해서 비율구하기
df.loc[df['gender']=='M','gender']=0
df.loc[df['gender']=='F','gender']=1

groups=df.groupby('occupation')
groups.mean()['gender'].sort_values(ascending=False)

#merge(합치기)
#관계있는 두 DataFrame을 합침

pd.merge(price_df,quantity_df,on='Product',how='inner')
#how 생략하면 기본으로 'inner'가 들어가고
#left,right,outer등이 있음

```


