from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from EmolayPolls.celery import app

from fpdf import FPDF

@app.task
def create_pdf(user_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f'name: {user_name}', ln=1, align="C")
    pdf.output(f"{user_name}.pdf")
