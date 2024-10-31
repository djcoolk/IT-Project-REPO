const APP_ID = "702d01c8ad8344cb88e485e096e41115";
const TOKEN = "007eJxTYDgWkferUuXOfpHVabGKJ1w2brgxo+2OkPmKPaX7pmnwOvopMJgbGKUYGCZbJKZYGJuYJCdZWKSaWJimGliapZoYGhqa+l0VSG8IZGQI61FlZWSAQBCfhSE3MTOPgQEAQ6geQw==";
const CHANNEL = "main";

const client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });

let localTracks = [];
let remoteUsers = {};

let joinAndDisplayLocalStream = async () => {
    try {
        client.on('user-published', handleUserJoined);
        client.on('user-left', handleUserLeft);
        
        let UID = await client.join(APP_ID, CHANNEL, TOKEN, null);
        console.log("User ID: ", UID);
        
        localTracks = await AgoraRTC.createMicrophoneAndCameraTracks();
        console.log("Local tracks created: ", localTracks);

        let player = `<div class="video-container" id="user-container-${UID}">
                          <div class="video-player" id="user-${UID}"></div>
                      </div>`;
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);
        localTracks[1].play(`user-${UID}`);
        console.log(`Playing local video in element: user-${UID}`);

        await client.publish([localTracks[0], localTracks[1]]);
        console.log("Published local tracks");
    } catch (error) {
        console.error('Error joining stream:', error);
    }
};

let joinStream = async () => {
    await joinAndDisplayLocalStream();
    document.getElementById('join-btn').style.display = 'none';
    document.getElementById('stream-controls').style.display = 'flex';
};

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user;
    await client.subscribe(user, mediaType);

    if (mediaType === 'video') {
        let player = document.getElementById(`user-container-${user.uid}`);
        if (player) {
            player.remove();
        }

        player = `<div class="video-container" id="user-container-${user.uid}">
                      <div class="video-player" id="user-${user.uid}"></div>
                  </div>`;
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);
       user.videoTrack.play(`user-${user.uid}`);
        console.log(`Playing remote user video in element: user-${user.uid}`);
    }

    if (mediaType === 'audio') {
        user.audioTrack.play();
    }
};

let handleUserLeft = async (user) => {
    delete remoteUsers[user.uid];
    let player = document.getElementById(`user-container-${user.uid}`);
    if (player) {
        player.remove();
    }
};

let leaveAndRemoveLocalStream = async () => {
    try {
        for (let i = 0; i < localTracks.length; i++) {
            localTracks[i].stop();
            localTracks[i].close();
        }

        await client.leave();
        document.getElementById('join-btn').style.display = 'block';
        document.getElementById('stream-controls').style.display = 'none';
        document.getElementById('video-streams').innerHTML = '';
    } catch (error) {
        console.error('Error leaving stream:', error);
    }
};

let toggleMic = async (e) => {
    if (localTracks[0].muted) {
        await localTracks[0].setMuted(false);
        e.target.innerText = 'Mic on';
        e.target.style.backgroundColor = 'cadetblue';
    } else {
        await localTracks[0].setMuted(true);
        e.target.innerText = 'Mic off';
        e.target.style.backgroundColor = '#EE4B2B';
    }
};

let toggleCamera = async (e) => {
    if (localTracks[1].muted) {
        await localTracks[1].setMuted(false);
        e.target.innerText = 'Camera on';
        e.target.style.backgroundColor = 'cadetblue';
    } else {
        await localTracks[1].setMuted(true);
        e.target.innerText = 'Camera off';
        e.target.style.backgroundColor = '#EE4B2B';
    }
};

document.getElementById('join-btn').addEventListener('click', joinStream);
document.getElementById('leave-btn').addEventListener('click', leaveAndRemoveLocalStream);
document.getElementById('mic-btn').addEventListener('click', toggleMic);
document.getElementById('camera-btn').addEventListener('click', toggleCamera);
