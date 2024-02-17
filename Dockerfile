FROM python:3.10 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src . 
ENV PATH=/root/.local:$PATH
ENV HOST=0.0.0.0

CMD ["python3", "/app"]