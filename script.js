const repositoryList = document.querySelector("#repository-list");
const repositoryCount = document.querySelector("#repository-count");

function formatStars(stars) {
  return new Intl.NumberFormat().format(stars);
}

function createRepositoryCard(repository) {
  const article = document.createElement("article");
  article.className = "repository-card";

  const title = document.createElement("h3");
  const link = document.createElement("a");
  link.href = repository.url;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = repository.name;
  title.append(link);

  const description = document.createElement("p");
  description.textContent = repository.description;

  const metadata = document.createElement("div");
  metadata.className = "repository-meta";
  metadata.innerHTML = `
    <span>★ ${formatStars(repository.stars)} stars</span>
    <span>${repository.language}</span>
    <time datetime="${repository.starredOn}">Starred ${repository.starredOn}</time>
  `;

  article.append(title, description, metadata);
  return article;
}

async function loadRepositories() {
  try {
    const response = await fetch("events.json");
    if (!response.ok) {
      throw new Error(`Unable to load repositories (${response.status})`);
    }

    const repositories = await response.json();
    repositoryList.replaceChildren(
      ...repositories.map(createRepositoryCard)
    );
    repositoryCount.textContent = `${repositories.length} repositories`;
  } catch (error) {
    repositoryList.replaceChildren();
    const message = document.createElement("p");
    message.className = "status error";
    message.textContent = "Could not load starred repositories. Please try again later.";
    repositoryList.append(message);
    console.error(error);
  }
}

loadRepositories();
