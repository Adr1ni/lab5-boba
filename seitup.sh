clone_repository() {
  local repo_url="https://github.com/Adr1ni/lab5-boba"
  if [ ! -d "exam-boba" ]; then
    echo "Cloning the repository..."
    git clone $repo_url
  else
    echo "Repository already cloned."
  fi
}

build_and_run_container() {
  cd lab5-boba

  echo "Running Docker..."
  docker build -t hola-mundo-multiple .

  echo "Running Docker..."
  docker run --rm hola-mundo-multiple

  cd kafka
  docker compose up -d
}

clone_repository
build_and_run_container