# Medical Shop AI — System Architecture

## 1. Problem

A chemist receives prescriptions and needs to identify the medicines,
understand the required information, and locate the medicines inside
the medical shop.

## 2. Proposed Solution

The system will accept a prescription image, extract medicine
information using OCR / AI vision, identify medicines using AI,
retrieve verified medicine information, and find the corresponding
shelf location from the shop's inventory database.

## 3. High-Level Pipeline

Prescription Image
        ↓
OCR / Vision
        ↓
Extracted Text
        ↓
Medicine Extraction
        ↓
Medicine Database
        ↓
Medicine Information + Shelf Location
        ↓
Chemist Interface

## 4. AI Components

- OCR / Computer Vision
- Natural Language Processing
- Large Language Models
- Retrieval / RAG

## 5. Non-AI Components

- Backend API
- SQL Database
- Inventory Management
- Shelf Mapping
- Frontend Interface

## 6. Initial MVP

The first version will focus on:

1. Prescription image upload
2. Text extraction
3. Medicine identification
4. Medicine database lookup
5. Shelf number display

## 7. Development Philosophy

Learn → Experiment → Implement → Test → Document → Commit