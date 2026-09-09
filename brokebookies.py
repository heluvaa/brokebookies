import json
import os
import random  # Tambahan untuk random delay & UA
import time
import requests

# ==========================================
# BROKE BOOKIES EARLY ACCESS AUTO SUBMITTER
# ==========================================

URL = "https://brokebookies.com/api/early-access"


def load_user_agents():
  ua_file = "user-agent.txt"
  if not os.path.exists(ua_file):
    default_ua = (
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like"
        " Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"
    )
    with open(ua_file, "w") as f:
      f.write(default_ua + "\n")
    return [default_ua]

  with open(ua_file, "r") as f:
    uas = [
        line.strip() for line in f if line.strip() and not line.startswith("#")
    ]
  return (
      uas
      if uas
      else [
          "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like"
          " Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"
      ]
  )


def submit_wallet(wallet, user_agent):
  headers = {
      "accept": "*/*",
      "accept-language": "id-ID",
      "content-type": "application/json",
      "origin": "https://brokebookies.com",
      "priority": "u=1, i",
      "sec-ch-ua": (
          '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge'
          ' Simulate";v="127", "Lemur";v="127"'
      ),
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-platform": '"Android"',
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "user-agent": user_agent,
  }

  payload = {"wallet": wallet.strip()}
  try:
    response = requests.post(URL, headers=headers, json=payload, timeout=10)
    return response.status_code, response.text
  except requests.exceptions.RequestException as e:
    return 0, str(e)


def main():
  print("=" * 50)
  print("   BROKE BOOKIES EARLY ACCESS AUTO SUBMITTER   ")
  print("=" * 50)

  wallet_file = "evm.txt"
  if not os.path.exists(wallet_file):
    print(f"[ERROR] File '{wallet_file}' tidak ditemukan!")
    return

  with open(wallet_file, "r") as f:
    wallets = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

  if not wallets:
    print(f"[WARNING] File '{wallet_file}' kosong.")
    return

  user_agents = load_user_agents()
  print(
      f"[INFO] Total wallet: {len(wallets)} | Total User-Agent:"
      f" {len(user_agents)}"
  )
  print(
      "[INFO] Menggunakan jeda waktu acak (3 - 6 detik) untuk menghindari"
      " 429 Too Many Requests...\n"
  )

  success_count = 0
  fail_count = 0

  for idx, wallet in enumerate(wallets, 1):
    # Pilih User-Agent secara acak dari file user-agent.txt
    current_ua = random.choice(user_agents)

    print(f"[{idx}/{len(wallets)}] Mengirim wallet: {wallet} ... ", end="")
    status_code, response_text = submit_wallet(wallet, current_ua)

    if status_code in [200, 201]:
      print(f"SUKSES (Status: {status_code})")
      success_count += 1
    else:
      print(f"GAGAL (Status: {status_code}) - {response_text}")
      fail_count += 1

      # Jika terkena rate limit (429), berikan jeda tambahan yang lebih lama secara otomatis
      if status_code == 429:
        print(
            "       [!] Terkena Rate Limit (429). Istirahat sejenak 10"
            " detik..."
        )
        time.sleep(10)

    # Jeda acak normal antar request (misal antara 3 sampai 6 detik) agar terlihat seperti manusia
    sleep_time = random.uniform(3.0, 6.0)
    time.sleep(sleep_time)

  print("\n" + "=" * 50)
  print(f"SELESAI! Berhasil: {success_count} | Gagal: {fail_count}")
  print("=" * 50)


if __name__ == "__main__":
  main()
