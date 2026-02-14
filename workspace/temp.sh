#!/bin/bash

set -e

# Where files will be created
BASE_DIR="./generated_code"

mkdir -p "$BASE_DIR/python"
mkdir -p "$BASE_DIR/go"
mkdir -p "$BASE_DIR/rust"

random_name() {
  cat /dev/urandom | tr -dc a-z | head -c 8
}

generate_python() {
  file=$1
  echo "# Auto generated Python file" > "$file"
  echo "" >> "$file"
  for i in $(seq 1 100); do
    echo "def func_$i():" >> "$file"
    echo "    return $i" >> "$file"
    echo "" >> "$file"
  done
}

generate_go() {
  file=$1
  echo "// Auto generated Go file" > "$file"
  echo "package main" >> "$file"
  echo "" >> "$file"
  for i in $(seq 1 100); do
    echo "func func$i() int {" >> "$file"
    echo "    return $i" >> "$file"
    echo "}" >> "$file"
    echo "" >> "$file"
  done
}

generate_rust() {
  file=$1
  echo "// Auto generated Rust file" > "$file"
  echo "" >> "$file"
  for i in $(seq 1 100); do
    echo "fn func_$i() -> i32 {" >> "$file"
    echo "    $i" >> "$file"
    echo "}" >> "$file"
    echo "" >> "$file"
  done
}

echo "Generating Python files..."
for i in {1..3}; do
  name=$(random_name)
  generate_python "$BASE_DIR/python/${name}.py"
done

echo "Generating Go files..."
for i in {1..3}; do
  name=$(random_name)
  generate_go "$BASE_DIR/go/${name}.go"
done

echo "Generating Rust files..."
for i in {1..3}; do
  name=$(random_name)
  generate_rust "$BASE_DIR/rust/${name}.rs"
done

echo "✅ Done. Files created in $BASE_DIR"
