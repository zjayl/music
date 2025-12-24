import streamlit as st

# 页面配置
st.set_page_config(page_title="网络版音乐播放器", layout="centered")

# 歌曲列表（使用网络音频URL + 网络专辑封面URL，无需本地文件）
SONGS = [
    {
        "title": "晴天",
        "artist": "周杰伦",
        "cover": "https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/109951168875636995.jpg",  # 专辑图URL
        "audio_url": "https://music.163.com/song/media/outer/url?id=186016.mp3"  # 音频URL
    },
    {
        "title": "花海",
        "artist": "周杰伦",
        "cover": "https://p2.music.126.net/7TL2p35K9x0478-0WeY4kw==/109951168874863260.jpg",
        "audio_url": "https://music.163.com/song/media/outer/url?id=25644881.mp3"
    },
    {
        "title": "七里香",
        "artist": "周杰伦",
        "cover": "https://p2.music.126.net/65DgwN47KOMQY887VY28gg==/109951168874863262.jpg",
        "audio_url": "https://music.163.com/song/media/outer/url?id=25644877.mp3"
    }
]

# 初始化当前播放歌曲索引
if "current_song_idx" not in st.session_state:
    st.session_state.current_song_idx = 0

def main():
    st.title("🎵 网络版音乐播放器")
    st.caption("无需本地文件，直接播放网易云音乐URL")

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