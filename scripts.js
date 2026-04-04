let userAccount = null;

// connect
document.getElementById("connectWallet").onclick = async () => {
    if (window.ethereum) {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        userAccount = accounts[0];

        document.getElementById("owner").value = userAccount;
        document.getElementById("accountInfo").innerText = userAccount;

        document.getElementById("connectWallet").style.display = "none";
        document.getElementById("disconnectWallet").style.display = "inline";
    }
};

// disconnect
document.getElementById("disconnectWallet").onclick = () => {
    userAccount = null;
    document.getElementById("accountInfo").innerText = "";
};

// forms
async function sendForm(id, url) {
    document.getElementById(id).onsubmit = async (e) => {
        e.preventDefault();

        const formData = new FormData(e.target);

        document.getElementById("loader").style.display = "block";

        const res = await fetch(url, { method: "POST", body: formData });
        const data = await res.json();

        document.getElementById("result").innerText = data.result;

        document.getElementById("loader").style.display = "none";
    };
}

sendForm("registerForm", "/register");
sendForm("updateForm", "/update");
sendForm("transferForm", "/transfer");
sendForm("resolveForm", "/resolve");