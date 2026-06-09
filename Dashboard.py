import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

# st.image(r'C:\Users\welcome\Desktop\BSMS1306\streamlit\Header.png')
st.image('Header.jpg')
st.set_page_config(page_title="BSMS 1306 Mini Project", layout="centered")
st.title("""BSMS 1306 Mini Project""")

st.markdown("""
### Group Members:
* **NAME:** MUHAMMAD AQIB BHAIS BIN SUKRI - 2513363
* **NAME:** AHMADINEJAD AL HELMI BIN AIDI HELMI - 2510999
""")

# upload data
# upload_file = st.file_uploader("Please upload here:", type='csv')

# df = pd.read_csv(r"C:\Users\welcome\Desktop\BSMS1306\streamlit\Tips.csv")
df = pd.read_csv("Gaming_Academic_Performance.csv")
# df = pd.read_csv(upload_file)

df.columns = df.columns.str.capitalize()
df.columns = df.columns.str.replace('_', ' ')

df['Gaming hours'] = df['Gaming hours'].astype('int')
df['Study hours'] = df['Study hours'].astype('int')
df['Sleep hours'] = df['Sleep hours'].astype('int')
df[['Grades']] = df[['Grades']].round(2)


# show data
st.subheader("Raw Dataset of Gaming Academic Performance")
st.write(df)

# ---------------------------
# OBJECTIVE 1
# ---------------------------

st.subheader("Objective 1: The Relationship between gaming hour, sleep hour, and attendance with grades")
st.subheader("🕹️Gaming hour, Sleep hour and Attendance vs. Student Grades")
st.markdown("Choose a metric from the dropdown below to see how it changes across different grade levels.")

metric_options = {
    "Weekly Gaming Hours": {"col": "Gaming hours", "color": "red"},
    "Daily Sleep Hours": {"col": "Sleep hours", "color": "green"},
    "Attendance Rate (%)": {"col": "Attendance", "color": "purple"}
}
selected = st.selectbox("Select metric for Y-Axis:", list(metric_options.keys()))

df['Grades'] = df['Grades'].clip(0, 100).round()

avg_df = df.groupby("Grades")[metric_options[selected]["col"]].mean().reset_index()

fig = px.line(
    avg_df,
    x="Grades",
    y=metric_options[selected]["col"],
    markers=True,
    title=f"Average {selected} Trend by Student Grades",
    color_discrete_sequence=[metric_options[selected]["color"]],
    template="plotly_white",
    labels={"Grades": "Grades (%)", metric_options[selected]["col"]: "Average Value"}
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# OBJECTIVE 2
# ---------------------------
st.subheader("Objective 2: The Relationship between gaming hours and students’ academic performance (grades).")

st.set_page_config(page_title="Stress vs Addiction", layout="centered")
st.subheader("⏰ Gaming Hours vs. Student Grades")
st.markdown("This line chart visualizes the precise downward trajectory of average academic scores as weekly gaming hours accumulate.")

gaming_grades = df.groupby("Gaming hours")["Grades"].mean()
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(
    gaming_grades.index,
    gaming_grades.values,
    marker="x",
    linestyle="-",
    color="purple",
)
ax1.set_title("Average Grades Trend by Gaming Hours")
ax1.set_xlabel("Gaming hours")
ax1.set_ylabel("Average Grades")
ax1.grid(True)
st.pyplot(fig1)

# ---------------------------
# OBJECTIVE 3
# ---------------------------

st.subheader("Objective 3:To explore whether gender plays a role in the types of video games students choose to play. ")

st.set_page_config(page_title="Genre by Gender", layout="centered")
st.subheader("⚥ Gaming Genre Distribution by Gender")
st.markdown("Explores demographic variations in video game preference between genders.")

fig, ax = plt.subplots(figsize=(9, 5))
gender_genre = df.groupby(['Gender', 'Gaming genre']).size().reset_index(name='count')

sns.barplot(data=gender_genre, x='Gaming genre', y='count', hue='Gender', ax=ax, palette='muted')
ax.set_xlabel('Gaming Genre')
ax.set_ylabel('Count')

st.pyplot(fig)

# ---------------------------
# OBJECTIVE 4 
# ---------------------------

st.subheader("Objective 4: Effect of Gaming Addiction and Stress on Grades")

st.set_page_config(page_title="Stress vs Addiction", layout="centered")
st.subheader("🧠 Stress Levels vs. Gaming Addiction Score")
st.markdown("Observes if students experiencing higher stress segments also map to elevated addiction parameters.")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='Stress level', y='Addiction score', ax=ax, order=['Low', 'Medium', 'High'], palette='Reds')
ax.set_xlabel('Stress Level')
ax.set_ylabel('Gaming Addiction Score')

st.pyplot(fig)

# ---------------------------
