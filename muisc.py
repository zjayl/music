import streamlit as st

# 页面配置
st.set_page_config(page_title="网络版音乐播放器", layout="centered")
SONGS = [
    {
        "title": "卡农 (钢琴版)",
        "artist": "经典纯音乐",
        "cover": "https://raw.githubusercontent.com/JoeyBling/ImageHosting/master/music_covers/canon.jpg",  # 永久专辑图
        "audio_url": "https://raw.githubusercontent.com/JoeyBling/ImageHosting/master/music/canon.mp3"       # 永久音频
    },
    {
        "title": "致爱丽丝",
        "artist": "贝多芬",
        "cover": "https://raw.githubusercontent.com/JoeyBling/ImageHosting/master/music_covers/elise.jpg",
        "audio_url": "https://raw.githubusercontent.com/JoeyBling/ImageHosting/master/music/elise.mp3"
    },
    {
        "title": "小星星 (经典版)",
        "artist": "经典儿歌",
        "cover": "https://raw.githubusercontent.com/JoeyBling/ImageHosting/master/music_covers/star.jpg",
        "audio_url": "https://raw.githubusercontent.com/JoeyBling/ImageHosting/master/music/star.mp3"
    }
]

# 初始化当前播放歌曲索引
if "current_song_idx" not in st.session_state:
    st.session_state.current_song_idx = 0

def main():
    st.title("🎵 网络版音乐播放器")

    # 获取当前歌曲信息
    current_song = SONGS[st.session_state.current_song_idx]

    # 布局：专辑图 + 歌曲信息
    col1, col2 = st.columns([1, 2])
    with col1:
        # 显示专辑封面（网络URL）
        st.image(current_song["cover"], caption="专辑封面", width=180)
    with col2:
        st.subheader(f"🎶 {current_song['title']}")
        st.write(f"🎤 歌手：{current_song['artist']}")
        # 播放网络音频（直接传入URL）
        st.audio(current_song["audio_url"], format="audio/mp3")

    # 切换歌曲按钮
    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("⏮️ 上一首"):
            st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(SONGS)
            st.rerun()  # 新版Streamlit用st.rerun()替代旧版rerun
    with col_next:
        if st.button("⏭️ 下一首"):
            st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(SONGS)
            st.rerun()

if __name__ == "__main__":

    main()

