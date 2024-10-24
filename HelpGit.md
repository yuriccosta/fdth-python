# Colinha para o git

## Iniciando

Na primeira vez, abra o terminal e digite:

```
git clone https://github.com/yuriccosta/calendario_UESC
```

## Puxando atualizações

Sempre que for iniciar o trabalho utilize o comando `git pull` para pegar as atualizações que outras pessoas podem ter feito

## Divisão de branchs

Foi divido em 3 branchs

- `develop` onde fica o código em desenvolvimento
- `test` onde fica o código desenvolvido que precisa ser testado
- `main` onde fica o código já testado e pronto

## Entre na sua branch

Para entrar na branch:

``` bash
git checkout "Nome da sua branch"
```

Por exemplo, para mudar para a branch `main`, `test` ou `develop`, você usaria:

```
git checkout main
git checkout test
git checkout develop
```

## Adicionando modificações

Adicionou um novo método, classe ou arquivo?  
Agora tem que adicionar essa mudança, para isso utilize o comando `git add`

Por exemplo, para adicionar todas as mudanças que fez:

```bash
git add .
```

Ou adicione apenas o que deseja, passando o caminho do arquivo, nome da pasta com:

``` bash
git add pasta2/arquivo1 pasta1 
```

## Fazendo Commits

Depois de adicionar os arquivos, faça um `git commit` e adicione um comentário sobre o que foi adicionado. Por exemplo:

```bash
git commit -m "Adicionado a classe dos dias"
```

## Suba seu código

Depois de fazer o commit suba suas alterações para que todos possam ver com o comando `git push`. Por exemplo, para subir suas alterações para a branch `main`:

```bash
git push origin main
```

Lembre-se de substituir `main` pelo nome da branch para a qual você deseja subir suas alterações.

## Pull Request

### Para quem estiver na develop

- Quando achar que está pronto para mandar para a test, vá no github nesse repositório e entre na aba Pull requests
- Selecione New pull request
- No primeiro slot selecione a branch `test` e no segundo selecione a branch `develop`
- Selecione Create pull request
- Dê um título e uma descrição, confirme o PR e avise que o fez

### Para quem estiver na test

Se o código enviado pela develop estiver correto

- Vá no github nesse repositório e entre na aba Pull requests
- Selecione New pull request
- No primeiro slot selecione a branch `main` e no segundo selecione a branch `test`
- Selecione Create pull request
- Dê um título e uma descrição, confirme o PR e avise que o fez

Se o código tiver erros ou ainda não estiver pronto para ir para main

- Vá no github nesse repositório e entre na aba Pull requests
- Selecione New pull request
- No primeiro slot selecione a branch `develop` e no segundo selecione a branch `test`
- Selecione Create pull request
- Dê um título e uma descrição, confirme o PR e avise que o fez
