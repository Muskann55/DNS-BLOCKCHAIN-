This project focuses on backend design, API clarity, and system architecture rather than production complexity.This project implements a decentralized DNS system with basic security considerations, focusing on clean backend design, well-structured APIs, and clear system architecture rather than unnecessary production complexity.
# 🌐 Decentralized DNS System using Blockchain

> A secure, transparent, and decentralized Domain Name System (DNS) built using Blockchain and Smart Contracts to eliminate single points of failure, prevent DNS spoofing, and provide tamper-proof domain management.

![Blockchain](https://img.shields.io/badge/Blockchain-Ethereum-blue)
![Solidity](https://img.shields.io/badge/Solidity-Smart%20Contracts-black)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-Backend-green)
![License](https://img.shields.io/badge/License-MIT-orange)

---

# 📌 Project Overview

Traditional DNS systems rely on centralized servers, making them vulnerable to:

- DNS Spoofing
- DNS Hijacking
- Single Point of Failure
- Censorship
- Unauthorized Record Modification

Our project introduces a **Blockchain-Based Decentralized DNS** where all domain records are securely stored on the blockchain and managed through smart contracts.

Only verified owners can modify domain records, while every transaction is permanently recorded for complete transparency.

---

# 🎯 Objectives

- Secure Domain Registration
- Immutable DNS Records
- Blockchain-based Ownership Verification
- Transparent Audit Logs
- Eliminate Centralized DNS Attacks
- Fast Domain Resolution
- Decentralized Governance

---

# 🚀 Features

### 🔐 Wallet Authentication
- MetaMask Login
- WalletConnect Support
- Secure Digital Identity

### 🌍 Domain Management
- Register Domain
- Update DNS Records
- Renew Domain
- Transfer Ownership
- Domain Lookup

### ⛓ Blockchain Security
- Smart Contract Validation
- Immutable Records
- Ownership Verification
- Event Logging

### 📄 DNS Records
Supports

- A Record
- AAAA Record
- TXT Record
- MX Record
- CNAME
- IPFS Hash

### 💳 Payment
- Registration Fee
- Renewal Fee
- On-chain Payment
- Gas Fee Calculation

### 📊 Transparency
- Audit Logs
- Transaction History
- Blockchain Explorer Integration

### ⚖ Governance
- Validator Approval
- Multi-Signature Voting
- Protected Domain Management

---

# 🛠 Tech Stack

## Frontend

- React.js
- HTML5
- CSS3
- JavaScript
- Bootstrap

## Backend

- Node.js
- Express.js

## Blockchain

- Ethereum
- Solidity
- Hardhat
- Ganache
- MetaMask

## Database

- MongoDB / MySQL (Optional)

## Storage

- IPFS

## APIs

- Infura
- Ethers.js
- Web3.js

---

# 📂 Project Structure

```
Decentralized-DNS
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── assets/
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   └── server.js
│
├── smart-contract/
│   ├── contracts/
│   ├── scripts/
│   ├── test/
│   └── hardhat.config.js
│
├── resolver/
│
├── docs/
│
├── screenshots/
│
└── README.md
```

---

# 🔄 Workflow

```
User
   │
   ▼
Connect Wallet
   │
   ▼
Verify Identity
   │
   ▼
Choose Action
(Register / Update / Lookup)
   │
   ▼
Frontend DApp
   │
   ▼
Smart Contract
   │
   ▼
Blockchain
   │
   ▼
Store DNS Records
   │
   ▼
Audit Log
   │
   ▼
Custom DNS Resolver
   │
   ▼
Verified DNS Response
```

---

# 🗄 Database Design

Entities

- User
- Wallet
- Domain
- DNS Record
- Payment
- Smart Contract
- Governance
- Audit Log

---

# 🔒 Security Features

✔ Wallet Authentication

✔ Blockchain Ownership Verification

✔ Immutable Records

✔ Event Logging

✔ Multi-Signature Governance

✔ Transparent Audit Trail

✔ DNS Spoofing Protection

✔ DNS Hijacking Prevention

---

# 💡 Innovation

Unlike traditional DNS systems, our platform introduces:

- Blockchain-based DNS Registry
- Trust Score for DNS Resolution
- Governance-based Protected Domains
- Transparent Audit Logs
- Decentralized Ownership Verification
- IPFS Integrated Content Storage

---

# 📸 Screenshots

## Home Page

(Add Screenshot)

## Wallet Login

(Add Screenshot)

## Register Domain

(Add Screenshot)

## Domain Dashboard

(Add Screenshot)

## Smart Contract Deployment

(Add Screenshot)

## Transaction History

(Add Screenshot)

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/decentralized-dns.git
```

Move into Project

```bash
cd decentralized-dns
```

Install Dependencies

```bash
npm install
```

Run Backend

```bash
npm run server
```

Run Frontend

```bash
npm start
```

Deploy Smart Contract

```bash
npx hardhat run scripts/deploy.js --network localhost
```

---

# 🧪 Testing

- Smart Contract Testing
- Wallet Authentication Testing
- DNS Resolution Testing
- Security Testing
- Performance Testing

---

# 📈 Future Scope

- AI-based Threat Detection
- Quantum Resistant Cryptography
- Mobile Application
- ENS Integration
- Cross-Chain DNS
- Decentralized CDN
- Zero Knowledge Proof Authentication
- Browser Plugin

---

# 👩‍💻 Contributors

**Muskan Tiwari**

Cybersecurity | Blockchain | Web3 Developer

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

🐛 Report issues

💡 Suggest improvements

---

## Made with ❤️ for Smart India Hackathon (SIH)
