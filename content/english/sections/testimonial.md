---
enable: true
title: "Projects"
description: |
  The Knowledgeable Computing and Reasoning (KRaCR) Lab at IIIT-Delhi focuses on Semantic Web, Knowledge Graphs, and Ontology-based reasoning to enhance machine-driven decision-making. By developing techniques for data integration, structured querying, and inferencing, the lab supports projects in legal informatics, healthcare, and environmental analytics, enabling efficient information retrieval and analysis.

# Testimonials

testimonials:
  - subheading: "Ontology Modelling and Enrichment"
    items:
      - name: "Enriching Ontologies using Cardinality, Union and Intersection Axioms"
        designation: "Monika Jain, Nikhil Sachdeva"
        avatar: "/images/avatar-sm.png"
        content: |
          Ontologies that are built automatically by learning systems scale well in terms of the number of concepts, relationships, and coverage. However, their quality is not good. Other axiom types, apart from simple subclass relations, are missing in these ontologies. In this project, we focus on extracting the minimum, maximum, and exact cardinality relations as well as the union and intersection axioms from text.
        button: https://firebasestorage.googleapis.com/v0/b/kracr-website.appspot.com/o/Publications%2Fbookchapter.pdf?alt=media&token=ec4ba408-e93f-4a5c-94f0-d4c839ba38e9
      
      - name: "ODPReco - An Ontology Design Pattern Recommendation System"
        designation: "Maleeha Arif Yasvi"
        avatar: "/images/avatar-sm.png"
        content: |
          Ontologies evolve over time due to changes in the domain and application requirements. Maintaining an ontology and keeping it up-to-date is challenging. Ontology Design Patterns (ODPs) can improve ontology quality, modularity, and reusability. We built a tool, ODPReco, to recommend possible ODPs by analyzing an ontology's lexical, structural, and behavioral aspects.
      
      - name: "OntoSeer - A Recommendation System to Improve the Quality of Ontologies"
        designation: "Pramit Bhattacharyya"
        avatar: "/images/avatar-sm.png"
        content: |
          Building an ontology is time-consuming and confusing, especially for beginners. OntoSeer is a tool that monitors ontology development and provides real-time suggestions for naming conventions, vocabulary reuse, ODP implementation, and axioms to improve ontology quality.
      
      - name: "Ontology Learning and Enrichment Benchmark"
        designation: "Anurag, Monika Jain"
        avatar: "/images/avatar-sm.png"
        content: |
          Ontology learning builds ontologies automatically from unstructured data. Several systems exist, but they have been tested on different datasets. We work on generating text with annotations to create benchmarks for ontology learning with various axioms.

  - subheading: "Description Logic Reasoning"
    items:
      - name: "Embeddings for EL++ Description Logic"
        designation: "Sutapa Mondal, Biswesh Mohapatra, Sumit Bhatia, Srinivasaraghavan"
        avatar: "/images/avatar-sm.png"
        content: |
          Knowledge graph embedding models focus on capturing graph structure but ignore ontology constraints. We work on mapping ontology classes and relations to an n-dimensional vector space while preserving relationships, enabling reasoning tasks like classification and consistency checking.
      
      - name: "OWL2Bench: A Benchmark for OWL 2 Reasoners"
        designation: "Gunjan Singh, Ashwat Kumar, Kanav Bhagat, Ritam Biswas, Sumit Bhatia"
        avatar: "/images/avatar-sm.png"
        content: |
          Ontology reasoners vary in performance and expressivity. OWL2Bench extends the University Ontology Benchmark (UOBM) with high-quality benchmarks covering OWL 2 constructs, enabling scalability testing with arbitrarily large ontologies.
      
      - name: "Ontology Reasoning on Resource Constrained Devices"
        designation: "Arushi Jain"
        avatar: "/images/avatar-sm.png"
        content: |
          Ontology reasoning is resource-intensive but beneficial for question-answering and knowledge consistency. We explore running ontology reasoners on constrained devices like Android phones and Raspberry Pi, measuring power consumption and feasibility.

  - subheading: "Knowledge Graphs"
    items:
      - name: "Knowledge Graphs for Legal Domain"
        designation: "Vidhi Sharma, Udit Bhati, Ayush Garg, Arham Ali, Abhyudit Badhul, Vikram Goel, Sandhya PR, Surya Prakash"
        avatar: "/images/avatar-sm.png"
        content: |
          Indian laws exist in different formats and are not digitized. We create a structured Knowledge Graph linking related sections across laws, enabling easy legal analytics and stakeholder interaction.
      
      - name: "Assessing the Quality of Knowledge Graphs"
        designation: "Nirali Arora"
        avatar: "/images/avatar-sm.png"
        content: |
          Knowledge Graphs (KGs) are built using manual, semi-automatic, or automatic methods. No direct quality metrics exist, so we develop metrics to assess KG quality directly, aiding improvement.
      
      - name: "Tool to Improve the Quality of Knowledge Graphs"
        designation: "Pragya Sethi, Nidhi Goyal, Ponnurangam Kumaraguru"
        avatar: "/images/avatar-sm.png"
        content: |
          Automatically generated Knowledge Graphs suffer from poor quality, especially with long sentences. We improve triple quality using heuristics and rules, enhancing the accuracy of Knowledge Graphs.
      
      - name: "A SPARQL to Cypher Transpiler"
        designation: "Lakshya Agrawal, Nikunj Singhal"
        avatar: "/images/avatar-sm.png"
        content: |
          SPARQL is the query language for RDF graphs, while Cypher is popular for Property Graphs. We develop a converter to bridge these two formats, enabling cross-platform querying.
      
      - name: "A Structured, Integrated Platform for Air Quality and Healthcare Data"
        designation: "Saad Ahmad, Sudhir Attri, Raghav Rathi, Vishal Kumar, Rahul Gupta, Tavpritesh Sethi, Ponnurangam Kumaraguru"
        avatar: "/images/avatar-sm.png"
        content: |
          Data from air pollution and healthcare are related but lack a common structure. Using Semantic Web technologies like OWL 2 and RDF, we integrate and link data for structured querying and analysis.
      
      - name: "An Ontology-based Recommendation System for Neonatologists"
        designation: "Monika Jain, Harpreet Singh"
        avatar: "/images/avatar-sm.png"
        content: |
          Preterm babies in NICUs need careful monitoring. We develop an ontology-based nutrition guideline system that captures neonate data and recommends the appropriate nutrition and feeding amounts.

_build:
  render: "never"
---