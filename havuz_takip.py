import streamlit as str
import pandas as pd
from datetime import datetime

# Sayfa Genişlik Ayarı
str.set_page_config(layout="wide", page_title="Site Havuz Takip Sistemi")

# ==========================================
# 🔐 GÜVENLİK / ŞİFRE KONTROLÜ
# ==========================================
# Buradaki '1234' kısmını kendinize göre değiştirebilirsiniz!
GIZLI_SIFRE = "5253" 

if 'giris_basarili' not in str.session_state:
    str.session_state.giris_basarili = False

if not str.session_state.giris_basarili:
    str.subheader("🔒 Site Havuz Takip Sistemi - Giriş")
    girilen_sifre = str.text_input("Lütfen Giriş Şifresini Yazın:", type="password")
    if str.button("Sisteme Giriş Yap"):
        if girilen_sifre == GIZLI_SIFRE:
            str.session_state.giris_basarili = True
            str.rerun()
        else:
            str.error("⚠️ Hatalı şifre girdiniz!")
    str.stop() # Şifre doğru değilse kodun kalanını çalıştırma

# ==========================================
# DİNAMİK SAKİN LİSTESİ OLUŞTURUCU
# ==========================================
bloklarin_sakinleri = {}

bloklarin_sakinleri["A Blok"] = [
    "Metin Aksoy (A1 01 / Kat Maliki)", "Gülten Aksoy (A1 01 / Eşi-Yakını)",
    "Murat Yılmaz (A1 02 / Kat Maliki)", "Selin Yılmaz (A1 02 / Eşi-Yakını)",
    "Ahmet Özdemir (A1 03 / Kat Maliki)", "Zeynep Özdemir (A1 03 / Eşi-Yakını)",
    "Mustafa Demir (A1 04 / Kat Maliki)", "Ayşe Demir (A1 04 / Eşi-Yakını)",
    "Hasan Kaya (A1 05 / Kat Maliki)", "Fatma Kaya (A1 05 / Eşi-Yakını)",
    "İbrahim Çelik (A1 06 / Kat Maliki)", "Emine Çelik (A1 06 / Eşi-Yakını)",
    "Ali Şahin (A1 07 / Kat Maliki)", "Hatice Şahin (A1 07 / Eşi-Yakını)",
    "Hüseyin Yıldız (A1 08 / Kat Maliki)", "Özlem Yıldız (A1 08 / Eşi-Yakını)",
    "Mehmet Öztürk (A1 09 / Kat Maliki)", "Canan Öztürk (A1 09 / Eşi-Yakını)",
    "Süleyman Aydın (A1 10 / Kat Maliki)", "Merve Aydın (A1 10 / Eşi-Yakını)",
    "Kadir Arslan (A1 11 / Kat Maliki)", "Dilek Arslan (A1 11 / Eşi-Yakını)",
    "Recep Polat (A1 12 / Kat Maliki)", "Seda Polat (A1 12 / Eşi-Yakını)",
    "Eren Kılıç (A1 13 / Kat Maliki)", "Büşra Kılıç (A1 13 / Eşi-Yakını)",
    "Caner Koç (A1 14 / Kat Maliki)", "Filiz Koç (A1 14 / Eşi-Yakını)",
    "Gökhan Kurt (A1 15 / Kat Maliki)", "Aslı Kurt (A1 15 / Eşi-Yakını)",
    "Deniz Özkan (A1 16 / Kat Maliki)", "Eda Özkan (A1 16 / Eşi-Yakını)"
]

bloklarin_sakinleri["B Blok"] = [
    "Alper Buzan (B1 01 / Kat Maliki)", "Duygu Buzan (B1 01 / Eşi-Yakını)",
    "Tolga Bilmen (B1 02 / Kat Maliki)", "Füsun Bilmen (B1 02 / Eşi-Yakını)",
    "Erhan Okkalıoğlu (B1 03 / Kat Maliki)", "Neşe Okkalıoğlu (B1 03 / Eşi-Yakını)",
    "Özlem Yazır (B1 04 / Kat Maliki)", "Doğan Canyaşar (B1 05 / Kat Maliki)",
    "Cem Yılmaz (B1 05 / Eşi-Yakını)", "Türkan Tuzcu (B1 06 / Kat Maliki)",
    "Kerem Tuzcu (B1 06 / Eşi-Yakını)", "Utku Özden (B1 07 / Kat Maliki)",
    "Özlem Özden (B1 07 / Eşi-Yakını)", "Ahmet Özdemir (B1 08 / Kat Maliki)",
    "Pınar Özdemir (B1 08 / Eşi-Yakını)", "Serdar Kaplan (B1 09 / Kat Maliki)",
    "Ebru Kaplan (B1 09 / Eşi-Yakını)", "Süleyman Ağaç (B1 10 / Kat Maliki)",
    "Hatice Ağaç (B1 10 / Eşi-Yakını)", "Aysel Tatlıcıoğlu (B1 11 / Kat Maliki)",
    "Onur Yaşar Tatlıcıoğlu (B1 11 / Eşi-Yakını)", "Eren Rızbanoğlu (B1 12 / Kat Maliki)",
    "Halil Yıldız (B1 13 / Kat Maliki)", "Seçil Çamlıkoca (B1 14 / Kat Maliki)",
    "Metin Çamlıkule (B1 14 / Eşi-Yakını)", "Eda Atalay (B1 15 / Kat Maliki)",
    "Emre Memo (B1 16 / Kat Maliki)", "Özlem Memo (B1 16 / Eşi-Yakını)",
    "Cemre Esemen (B1 17 / Kat Maliki)", "İnci Egemen (B1 17 / Eşi-Yakını)",
    "SFA Can Meral (B1 18 / Kat Maliki)", "Melek Meral (B1 18 / Eşi-Yakını)",
    "Perihan Aslanhan (B1 19 / Kat Maliki)", "Onurcan Çelik (B1 20 / Kat Maliki)",
    "Selin Çelik (B1 20 / Eşi-Yakını)", "Mahirbey (B1 21 / Kat Maliki)",
    "Ali Başlar (B1 22 / Kat Maliki)", "Sinem Taymaz (B1 22 / Eşi-Yakını)",
    "Müjdat Pelit (B1 24 / Kat Maliki)", "Nurali Çiftçi (B1 25 / Kat Maliki)",
    "Nurgül Çiftçi (B1 25 / Eşi-Yakını)", "Musa Ercan (B1 26 / Kat Maliki)",
    "Davut Çelik (B1 27 / Kat Maliki)", "Hande Çelik (B1 27 / Eşi-Yakını)"
]

bloklarin_sakinleri["C1 Blok"] = [
    "Güler Tıkır (C1 01 / Kat Maliki)", "Abdülkadir Yenigün (C1 02 / Kat Maliki)",
    "Melek Yenigün (C1 02 / Eşi-Yakını)", "Dilek Yenigün (C1 02 / Çocuk)",
    "Tevfik Ezici (C1 03 / Kat Maliki)", "Tuğba Ekici (C1 03 / Eşi-Yakını)",
    "Pelin Madran (C1 04 / Kat Maliki)", "Levent Mandran (C1 04 / Eşi-Yakını)",
    "Onur Eriş (C1 05 / Kat Maliki)", "Jale Tökez (C1 06 / Kat Maliki)",
    "Gözde Tufan (C1 06 / Eşi-Yakını)", "Hanife Suzan Bilal (C1 07 / Kat Maliki)",
    "Serhan Bilal (C1 07 / Eşi-Yakını)", "Cengiz Efe (C1 08 / Kat Maliki)",
    "Emine Efe (C1 08 / Eşi-Yakını)", "Erhan Ergül (C1 09 / Kat Maliki)",
    "Zahide Ergül (C1 09 / Eşi-Yakını)", "Wissam (C1 10 / Kat Maliki)",
    "Nuriye Er (C1 11 / Kat Maliki)", "Erdinç Kırgözoğlu (C1 12 / Kat Maliki)",
    "Müzeher Kırgözoğlu (C1 12 / Eşi-Yakını)", "Defne Kırgözoğlu (C1 12 / Çocuk)",
    "Ahmet Avcı (C1 13 / Kat Maliki)", "Süleyman Uyar (C1 14 / Kat Maliki)",
    "Zeynep Uyar (C1 14 / Eşi-Yakını)", "Mesut Taner (C1 15 / Kat Maliki)",
    "Emine Betül Taner (C1 15 / Eşi-Yakını)", "Şevim Özgen (C1 17 / Kat Maliki)",
    "Levent Ülgen (C1 17 / Eşi-Yakını)", "Şeyda Ay (C1 18 / Kat Maliki)",
    "Kadir Ay (C1 18 / Eşi-Yakını)", "İlker Sancak (C1 19 / Kat Maliki)",
    "Büşra Sancak (C1 19 / Eşi-Yakını)", "Mertcan İltar (C1 20 / Kat Maliki)",
    "Eda Uytun (C1 20 / Eşi-Yakını)", "Deniz Bilbay (C1 21 / Kat Maliki)",
    "Ahmet Akdağ (C1 22 / Kat Maliki)", "Zeynep Akdağ (C1 22 / Eşi-Yakını)",
    "Didem Hortoğlu (C1 23 / Kat Maliki)", "Halil Öz (C1 23 / Eşi-Yakını)",
    "Uygur Yüzeyiroğlu (C1 24 / Kat Maliki)", "Gülhan Yüzereroğlu (C1 24 / Eşi-Yakını)"
]

bloklarin_sakinleri["C2 Blok"] = [
    "Erkan Adıyaman (C2 01 / Kat Maliki)", "Berna Adıyaman (C2 01 / Eşi-Yakını)",
    "Gizem Sofuoğlu (C2 02 / Kat Maliki)", "Nisa Sofuoğlu (C2 02 / Eşi-Yakını)",
    "İnci Sofuoğlu (C2 02 / Çocuk)", "Selahattin Kasap (C2 03 / Kat Maliki)",
    "Saygın Kasap (C2 03 / Eşi-Yakını)", "Sezgin Uztemur (C2 04 / Kat Maliki)",
    "Emine Uztemur (C2 04 / Eşi-Yakını)", "Sadullah Batmaz (C2 05 / Kat Maliki)",
    "Hatice Batmaz (C2 05 / Eşi-Yakını)", "Fatih Muslu (C2 06 / Kat Maliki)",
    "Pınar Muslu (C2 06 / Eşi-Yakını)", "Ender Sayın (C2 07 / Kat Maliki)",
    "Selen Sayın (C2 07 / Eşi-Yakını)", "Ali Oğuz (C2 08 / Kat Maliki)",
    "Ayla Oğuz (C2 08 / Eşi-Yakını)", "Emre Özdoğan (C2 09 / Kat Maliki)",
    "Melisa Özdoğan (C2 09 / Eşi-Yakını)", "Murat Durmaz (C2 10 / Kat Maliki)",
    "Duygu Durmaz (C2 10 / Eşi-Yakını)", "Mehmet Ali Çirik (C2 11 / Kat Maliki)",
    "Sedanur Kılıç (C2 11 / Eşi-Yakını)", "Mithat Birden (C2 12 / Kat Maliki)",
    "Ebru Önal Birden (C2 12 / Eşi-Yakını)", "Ahmet Öztuna (C2 13 / Kat Maliki)",
    "Sibel Öztuna (C2 13 / Eşi-Yakını)", "Semiye Ateşli (C2 14 / Kat Maliki)",
    "Melih Şiren (C2 15 / Kat Maliki)", "Oya Şiren (C2 15 / Eşi-Yakını)",
    "Ali Tirit (C2 16 / Kat Maliki)", "Bahar Tirit (C2 16 / Eşi-Yakını)",
    "Can Otuzbiroğlu (C2 17 / Kat Maliki)", "Hatice Kodaman (C2 17 / Eşi-Yakını)",
    "Atilla Er (C2 18 / Kat Maliki)", "Özge Er (C2 18 / Eşi-Yakını)",
    "Emre Erdemir (C2 19 / Kat Maliki)", "Hilal Erdemir (C2 19 / Eşi-Yakını)",
    "Barış Kılınçoğlu (C2 20 / Kat Maliki)", "Fulya Kılınçoğlu (C2 20 / Eşi-Yakını)",
    "Birol Gezer (C2 21 / Kat Maliki)", "Onur Öztürk (C2 22 / Kat Maliki)",
    "Filiz Öztürk (C2 22 / Eşi-Yakını)", "Ozan Bozyiğit (C2 23 / Kat Maliki)",
    "Gökhan Ayçiçek (C2 24 / Kat Maliki)", "Merve Ayçiçek (C2 24 / Eşi-Yakını)"
]

bloklarin_sakinleri["C3 Blok"] = [
    "Mehmet Peynirci (C3 01 / Kat Maliki)", "Beste Peynirci (C3 01 / Eşi-Yakını)",
    "İsmail İmre (C3 02 / Kat Maliki)", "Ömer Aslankarasoy (C3 03 / Kat Maliki)",
    "Nilüfer Aslanboğa (C3 03 / Eşi-Yakını)", "Gül Muslu (C3 04 / Kat Maliki)",
    "Fatih Muslu (C3 04 / Eşi-Yakını)", "Burak Boylu (C3 05 / Kat Maliki)",
    "Aslı Boylu (C3 05 / Eşi-Yakını)", "Devrim Artan (C3 06 / Kat Maliki)",
    "Deniz Çakmakçı (C3 06 / Eşi-Yakını)", "Mehmet Doğan (C3 07 / Kat Maliki)",
    "Selda Doğan (C3 07 / Eşi-Yakını)", "Hasan İşçi (C3 08 / Kat Maliki)",
    "Hasret İşçi (C3 08 / Eşi-Yakını)", "Murat Dinçkal (C3 09 / Kat Maliki)",
    "Mehmet Özalp (C3 10 / Kat Maliki)", "Dilek Özalp (C3 10 / Eşi-Yakını)",
    "Aksel Nikola (C3 11 / Kat Maliki)", "Sahibe Nikola (C3 11 / Eşi-Yakını)",
    "Özkan Karaman (C3 12 / Kat Maliki)", "Aynur Karaman (C3 12 / Eşi-Yakını)",
    "Başar Yıldıztekin (C3 13 / Kat Maliki)", "Dilay Yıldıztekin (C3 13 / Eşi-Yakını)",
    "Mert Yaşar Kuru (C3 14 / Kat Maliki)", "Ayşegül Kuru (C3 14 / Eşi-Yakını)",
    "Bilal Kaymaz (C3 15 / Kat Maliki)", "Irmak Kaymaz (C3 15 / Eşi-Yakını)",
    "Şener Sarıkaya (C3 16 / Kat Maliki)", "Asli Efe (C3 16 / Eşi-Yakını)",
    "Onrcan Çaki (C3 17 / Kat Maliki)", "Esra Çaki (C3 17 / Eşi-Yakını)",
    "Mehmet Ali Çeliker (C3 18 / Kat Maliki)", "Şafak Özoğlu (C3 19 / Kat Maliki)",
    "Serap Özoğlu (C3 19 / Eşi-Yakını)", "Deniz Yazıcıoğlu (C3 20 / Kat Maliki)",
    "Can Akyol (C3 22 / Kat Maliki)", "Sude Akyol (C3 22 / Eşi-Yakını)",
    "Utku Yalçın (C3 23 / Kat Maliki)", "Gülçay Yalçın (C3 23 / Eşi-Yakını)",
    "Engin Kılıç (C3 24 / Kat Maliki)", "Merve Kılıç (C3 24 / Eşi-Yakını)",
    "Mustafa Taştan (C3 25 / Kat Maliki)", "Zeynep Taştan (C3 25 / Eşi-Yakını)",
    "Bulut Ekici (C3 26 / Kat Maliki)", "Rabia Ekici (C3 26 / Eşi-Yakını)",
    "Enis Demir (C3 27 / Kat Maliki)", "Pelin Demir (C3 27 / Eşi-Yakını)"
]

bloklarin_sakinleri["C4 Blok"] = [
    "Uğur Çakmak (C4 01 / Kat Maliki)", "Saliha Çakmak (C4 01 / Eşi-Yakını)",
    "Gürkan Güleç (C4 02 / Kat Maliki)", "Ece Güleç (C4 02 / Eşi-Yakını)",
    "Murat Türe (C4 03 / Kat Maliki)", "Berna Bilgin (C4 03 / Eşi-Yakını)",
    "Gökhan Avcı (C4 04 / Kat Maliki)", "Kübra Okutan (C4 05 / Kat Maliki)",
    "Büşra Okutan (C4 05 / Eşi-Yakını)", "Emin Aklar (C4 06 / Kat Maliki)",
    "Elif Aklar (C4 06 / Eşi-Yakını)", "Ayşe Özyılmaz (C4 07 / Kat Maliki)",
    "Leyla Yıkıldım (C4 08 / Kat Maliki)", "Bersu Karaca Yıkıldım (C4 08 / Eşi-Yakını)",
    "Ali Türeli (C4 09 / Kat Maliki)", "Nefise Türeli (C4 09 / Eşi-Yakını)",
    "Sezgin İzmir (C4 10 / Kat Maliki)", "Şahnisa İzmir (C4 10 / Eşi-Yakını)",
    "Raşit Özkan (C4 11 / Kat Maliki)", "Tuğçe Özkan (C4 11 / Eşi-Yakını)",
    "Bilge Ökten (C4 12 / Kat Maliki)", "Murat Dalgali (C4 13 / Kat Maliki)",
    "Funda Dalgali (C4 13 / Eşi-Yakını)", "Ege Karabuket (C4 14 / Kat Maliki)",
    "Ceyda Ceylan (C4 14 / Eşi-Yakını)", "Ferruh Peker (C4 15 / Kat Maliki)",
    "Sebahat Peker (C4 15 / Eşi-Yakını)", "İbrahim Çekerek (C4 16 / Kat Maliki)",
    "Gülhan Çekerek (C4 16 / Eşi-Yakını)", "Mustafa Can Akar (C4 17 / Kat Maliki)",
    "Ercan Yalçin (C4 18 / Kat Maliki)", "Gül Menekşe (C4 19 / Kat Maliki)",
    "Şenel Menekşe (C4 19 / Eşi-Yakını)", "Ebru Atalay (C4 20 / Kat Maliki)",
    "Serra Erdem (C4 20 / Eşi-Yakını)", "Yakup Postaci (C4 21 / Kat Maliki)",
    "Banu Postaci (C4 21 / Eşi-Yakını)", "Bariş Abakan (C4 22 / Kat Maliki)",
    "Aykut Örs (C4 23 / Kat Maliki)", "Hisami Şehitoğlu (C4 24 / Kat Maliki)",
    "Elif Şehitoğlu (C4 24 / Eşi-Yakını)", "Dilara Kaya (C4 25 / Kat Maliki)",
    "Sermihan Beyazyildirim (C4 26 / Kat Maliki)", "Ozan Beyazyildirim (C4 26 / Eşi-Yakını)",
    "Mustafa Kaplan (C4 27 / Kat Maliki)", "Emine Kaplan (C4 27 / Eşi-Yakını)"
]

bloklarin_sakinleri["D1 Blok"] = [
    "Muharrem Çatalkaya (D1 01 / Kat Maliki)", "Nil Çatalkaya (D1 01 / Eşi-Yakını)",
    "Yiğit Gökten (D1 02 / Kat Maliki)", "Gülşah Batırlı (D1 02 / Eşi-Yakını)",
    "Sultan Çetin (D1 03 / Kat Maliki)", "Murat Bakıcı (D1 04 / Kat Maliki)",
    "Seda Bakıcı (D1 04 / Eşi-Yakını)", "Fatma Taşkıran (D1 05 / Kat Maliki)",
    "Ömer Akmeşe (D1 06 / Kat Maliki)", "Defne Akpınar (D1 07 / Kat Maliki)",
    "Pelin Söke (D1 08 / Kat Maliki)", "Emrah Pala (D1 09 / Kat Maliki)",
    "Nurgün Beşün (D1 10 / Kat Maliki)", "Nilgün Ergüder (D1 11 / Kat Maliki)",
    "İsmail Sercan Sağlam (D1 12 / Kat Maliki)", "Batuhan Gündoğdu (D1 13 / Kat Maliki)",
    "Murat Tekel (D1 14 / Kat Maliki)", "Tahir Özer (D1 15 / Kat Maliki)",
    "Evren Aydın (D1 16 / Kat Maliki)", "Tayfun Akar (D1 17 / Kat Maliki)",
    "Onur Şahin (D1 18 / Kat Maliki)", "Buket Arıkan (D1 19 / Kat Maliki)",
    "Tolga Özuğur (D1 20 / Kat Maliki)", "Zeliha Özuğur (D1 20 / Eşi-Yakını)",
    "Erman Alpağu (D1 21 / Kat Maliki)", "Başak Alpağu (D1 21 / Eşi-Yakını)",
    "Mehmet Günyol Arıkan (D1 22 / Kat Maliki)", "Kürşat Aslan (D1 23 / Kat Maliki)",
    "Mustafa Kanpakoğlu (D1 24 / Kat Maliki)", "Burak Çelik (D1 25 / Kat Maliki)",
    "Sezen Özdemir (D1 26 / Kat Maliki)", "Muhsin Özdemir (D1 26 / Eşi-Yakını)",
    "Hüseyin Kaya (D1 27 / Kat Maliki)"
]

bloklarin_sakinleri["D2 Blok"] = [
    "Şeyhmuz Aksoy (D2 01 / Kat Maliki)", "Sözdar Aksoy (D2 01 / Eşi-Yakını)",
    "Selahattin Doğan (D2 02 / Kat Maliki)", "Derya Doğan (D2 02 / Eşi-Yakını)",
    "Şahin Aykaş (D2 03 / Kat Maliki)", "Macide Koyuncu (D2 04 / Kat Maliki)",
    "Uğur Kaya (D2 05 / Kat Maliki)", "Kevser Kaya (D2 05 / Eşi-Yakını)",
    "Hüseyin Özkoç (D2 06 / Kat Maliki)", "Meltem Özkoç (D2 06 / Eşi-Yakını)",
    "Oktay Çamcı (D2 07 / Kat Maliki)", "Cem Çağatay (D2 08 / Kat Maliki)",
    "Gülben Çağatay (D2 08 / Eşi-Yakını)", "Mehmet İnal (D2 09 / Kat Maliki)",
    "Irina Inal (D2 09 / Eşi-Yakını)", "Mehmet Tutkun (D2 10 / Kat Maliki)",
    "Nazım Toklu (D2 11 / Kat Maliki)", "Erdem Metin (D2 12 / Kat Maliki)",
    "Ceren Metin (D2 12 / Eşi-Yakını)", "Enes Şengül (D2 14 / Kat Maliki)",
    "Mustafa Büyükkeresteci (D2 15 / Kat Maliki)", "Mehmet Akif Sütçü (D2 16 / Kat Maliki)",
    "Mustafa Şalak (D2 17 / Kat Maliki)", "Ayla Şavlak (D2 17 / Eşi-Yakını)",
    "Erhan Akgöl (D2 18 / Kat Maliki)", "Gökhan Öztaş (D2 19 / Kat Maliki)",
    "Fatih Sümer (D2 20 / Kat Maliki)", "Nihal Sümer (D2 20 / Eşi-Yakını)",
    "Kazım Tokmak (D2 21 / Kat Maliki)", "Yasin Ağaç (D2 22 / Kat Maliki)",
    "Levent Adıgüzel (D2 23 / Kat Maliki)", "Abdülkadir Özmen (D2 24 / Kat Maliki)",
    "Cansın Alban (D2 25 / Kat Maliki)", "Deniz Belli (D2 26 / Kat Maliki)",
    "Mehmet Öksüz (D2 27 / Kat Maliki)"
]

blok_listesi = ["A Blok", "B Blok", "C1 Blok", "C2 Blok", "C3 Blok", "C4 Blok", "D1 Blok", "D2 Blok"]

# ==========================================
# HAFIZA VE TABLO AYARLARI
# ==========================================
if 'kayitlar' not in str.session_state:
    str.session_state.kayitlar = pd.DataFrame(columns=["Tarih", "Blok/Daire", "Sakin Adı", "Giriş Tipi", "Misafir Adı Soyadı", "Misafir Sayısı"])

if 'secili_blok_hafiza' not in str.session_state:
    str.session_state.secili_blok_hafiza = "A Blok"

# ==========================================
# GÖRSEL ARAYÜZ
# ==========================================
str.title("🏊‍♂️ Site Havuz Giriş Takip Sistemi")
str.markdown("---")

col1, col2 = str.columns([1, 2])

with col1:
    str.subheader("📝 Yeni Giriş Kaydı")
    
    varsayilan_index = blok_listesi.index(str.session_state.secili_blok_hafiza)
    secilen_blok = str.selectbox("Önce Blok Seçiniz:", options=blok_listesi, index=varsayilan_index)
    
    if secilen_blok != str.session_state.secili_blok_hafiza:
        str.session_state.secili_blok_hafiza = secilen_blok
        str.rerun()
    
    o_blogun_sakinleri = bloklarin_sakinleri.get(secilen_blok, [])
    secilen_sakin = str.selectbox("Sakin Seçiniz:", options=o_blogun_sakinleri)
    
    giris_tipi = str.radio("Giriş Tipi:", ["Kat Maliki / Sakin", "Misafir"])
    
    misafir_adi = "-"
    misafir_sayisi = 0
    if giris_tipi == "Misafir":
        misafir_adi = str.text_input("Misafir İsim Soyisim:", placeholder="Örn: Ahmet Yılmaz")
        misafir_sayisi = str.number_input("Misafir Sayısı:", min_value=1, max_value=10, value=1)
        
    kaydet_butonu = str.button("Girişi Kaydet", use_container_width=True)
    
    if kaydet_butonu:
        if giris_tipi == "Misafir" and (not misafir_adi.strip() or misafir_adi == "-"):
            str.error("⚠️ Lütfen misafirin adını ve soyadını yazınız!")
        else:
            yeni_veri = {
                "Tarih": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Blok/Daire": secilen_blok,
                "Sakin Adı": secilen_sakin,
                "Giriş Tipi": giris_tipi,
                "Misafir Adı Soyadı": misafir_adi,
                "Misafir Sayısı": misafir_sayisi
            }
            str.session_state.kayitlar = pd.concat([str.session_state.kayitlar, pd.DataFrame([yeni_veri])], ignore_index=True)
            str.success("✅ Giriş kaydı başarıyla eklendi!")

with col2:
    str.subheader("📊 Günlük Giriş Tablosu")
    if not str.session_state.kayitlar.empty:
        str.dataframe(str.session_state.kayitlar, use_container_width=True)
        
        str.markdown("---")
        str.subheader("🗑️ Hatalı Kayıt Silme")
        silinecek_index = str.number_input("Silmek istediğiniz satırın numarasını seçin:", min_value=0, max_value=len(str.session_state.kayitlar)-1, step=1, value=0)
        
        if str.button("Seçili Kaydı Listeden Sil", type="primary"):
            str.session_state.kayitlar = str.session_state.kayitlar.drop(silinecek_index).reset_index(drop=True)
            str.success(f"❌ {silinecek_index} numaralı satır silindi!")
            str.rerun()
            
        str.markdown("---")
        csv = str.session_state.kayitlar.to_csv(index=False).encode('utf-8')
        str.download_button("📥 Tabloyu Bilgisayara İndir (CSV)", data=csv, file_name="havuz_gunluk_kayitlar.csv", mime="text/csv")
    else:
        str.warning("Henüz bugün yapılmış bir havuz girişi bulunmuyor.")