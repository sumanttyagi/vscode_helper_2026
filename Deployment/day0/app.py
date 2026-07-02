import streamlit as st

class SocialNetwork:
    def __init__(self):
        self.network = {
            "Alice": {"Bob", "Charlie", "David", "Eve"},
            "Bob": {"Alice", "Charlie", "Frank", "Grace"},
            "Charlie": {"Alice", "Bob", "David", "Frank"}
        }

    def get_mutual_friends(self, user1, user2):
        return self.network.get(user1, set()) & self.network.get(user2, set())

    def get_all_unique_friends(self, user1, user2):
        return self.network.get(user1, set()) | self.network.get(user2, set())

    def get_exclusive_friends(self, user1, user2):
        return self.network.get(user1, set()) - self.network.get(user2, set())

    def get_unshared_friends(self, user1, user2):
        return self.network.get(user1, set()) ^ self.network.get(user2, set())

# --- Streamlit Web UI ---
st.title("👥 Social Network Analyzer")

app = SocialNetwork()
users = list(app.network.keys())

# Create two dropdown menus
col1, col2 = st.columns(2)
with col1:
    user1 = st.selectbox("Select User 1", users, index=0)
with col2:
    user2 = st.selectbox("Select User 2", users, index=1)

# Display results when the user clicks the button
if st.button("Analyze Connections"):
    st.subheader(f"Analysis for {user1} & {user2}")
    
    st.write(f"**1. Mutual Friends (Intersection):** {app.get_mutual_friends(user1, user2) or 'None'}")
    st.write(f"**2. All Unique Friends (Union):** {app.get_all_unique_friends(user1, user2)}")
    st.write(f"**3. Friends {user1} has that {user2} doesn't (Difference):** {app.get_exclusive_friends(user1, user2) or 'None'}")
    st.write(f"**4. Unique to each, but not shared (Symmetric Diff):** {app.get_unshared_friends(user1, user2) or 'None'}")